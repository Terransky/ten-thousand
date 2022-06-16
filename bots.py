"""Place in root of Project,
at same level as pyproject.toml
"""

from abc import ABC, abstractmethod
import builtins
import re
import random
import time
from randcrack import RandCrack
from ten_thousand.game import Game
from ten_thousand.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls()
            game = Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MiddlingMargaret(BaseBot):
    """MiddlingMargaret has a moderate playing style"""

    def _roll_bank_or_quit(self):

        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""

        if self.unbanked_points >= 500 or self.dice_remaining < 3:
            return "b"

        return "r"


class DaringDarla(BaseBot):
    """DaringDarla rolls whenever more than 1 dice remaining """

    def _roll_bank_or_quit(self):
        if self.dice_remaining == 1:
            return "b"

        return "r"


class MarkBot(BaseBot):
    """
    self.dice_remaining
    self.unbanked_points
    self.total_score
    """

    def __init__(self):
        from collections import Counter

        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None

    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 3,
            2: 4 / 9,
            3: 8 / 27 - 1 / 36,
            4: 16 / 81 - 1 / 36,
            5: 32 / 243 - 1 / 36,
            6: 64 / 729 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]

    def _roll_bank_or_quit(self):
        # always roll when you have 6 dice to roll
        if not self.dice_remaining or self.dice_remaining == 6:
            return "r"
        # bank if we think we have a high chance of failure
        if MarkBot.chance_to_fail(self.dice_remaining) > 95 / (
            self.unbanked_points + 1
        ):
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 175:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        self.report("> " + roll_string)
        return roll_string


class YoniBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 550 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"


class DontFarkleUp(BaseBot):
    """Tony's bot"""

    def __init__(self):
        from collections import Counter

        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None
        self.last_roll = None

    def _roll_bank_or_quit(self):

        if self.unbanked_points >= 1000:  # immediately bank high score
            return "b"

        elif self.unbanked_points >= 400 and self.dice_remaining <= 2:  # bank if 2 or less dice remain
            return "b"

        elif self.unbanked_points < 400 and self.dice_remaining >= 3:  # roll if 3+ dice and low score
            return "r"

        elif self.unbanked_points >= 300 and self.dice_remaining < 3:  # bank if 2 or less dice and >=300 points
            return "b"

        elif self.unbanked_points < 300 and self.dice_remaining >= 2:  # roll if 2 or more dice and <300 points
            return "r"

        else:
            return "b"

    def _enter_dice(self):
        """
        I need methods to disregard low triples and roll again
        need methods to determine if double 5s, keep one 5, and roll again
        need to differentiate between two 5s and a 1, both are 100 points
        """

        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""

        if GameLogic.calculate_score(roll) >= 400:  # outputs roll, banks if few dice remaining
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string

        elif GameLogic.calculate_score(roll) < 400:  # checks for 1s and 5s to roll again since low score

            counter = self.Counter(roll)  # counts number of values, saves as object

            # self.real_print(self.last_roll)
            # self.real_print(counter)
            # self.real_print(roll)

            if counter[1] == 1 or counter[1] == 2:  # saves the 1, rolls again
                roll_string = "1"
                self.report("> " + roll_string)
                return roll_string

            elif counter[5] == 1 or counter[5] == 2:  # saves the 5, rolls again
                roll_string = "5"
                self.report("> " + roll_string)
                return roll_string

            elif self.dice_remaining >= 5 and counter[2] == 3:  # triple 2s, only  200 points, roll again
                return "r"

            elif self.dice_remaining >= 5 and counter[3] == 3:  # triple 3s, only  300 points, roll again
                return "r"

            else:

                if counter[4] == 3 or counter[2] == 4:  # if trip 4s or quad 2s
                    if counter[1] == 1 or counter[1] == 2:  # if there are 1s, keep one, roll again
                        roll_string = "1"
                        self.report("> " + roll_string)
                        return roll_string

                    elif counter[5] == 1 or counter[1] == 2:  # if there are 5s, keep one, roll again
                        roll_string = "5"
                        self.report("> " + roll_string)
                        return roll_string

                    else:  # return the roll for roll bank quit to decide
                        for value in roll:
                            roll_string += str(value)
                        self.report("> " + roll_string)
                        return roll_string

                # self.real_print(self.last_roll)
                # self.real_print(counter)
                # self.real_print(roll)
                else:
                    return "r"

        else:  # catch all

            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)

            return roll_string


class GamblingAnonymous(BaseBot):
    """JJ's bot"""
    def __init__(self):
        from collections import Counter

        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None

    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 5,
            2: 4 / 10,
            3: 8 / 30 - 1 / 36,
            4: 16 / 90 - 1 / 36,
            5: 32 / 250 - 1 / 36,
            6: 64 / 735 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]

    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 3000 or self.dice_remaining == 6:
            return "b"
        if not self.dice_remaining or self.dice_remaining == 5:
            return "r"
        if GamblingAnonymous.chance_to_fail(self.dice_remaining) > 100 / (
            self.unbanked_points + 1
        ):
            return "b"
        return "r"
        if self.unbanked_points >= 550 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining < 2:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 1:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"

    def _enter_dice(self):
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i: j + 2]):
                    test_dice = roll[i: j + 2]
                    test_score = GameLogic.calculate_score(roll[i: j + 1]) / len(
                        test_dice
                    )
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 500:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        self.report("> " + roll_string)
        return roll_string


class GamblingBotThree(BaseBot):
    """Jae's bot"""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None
    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 3,
            2: 4 / 9,
            3: 8 / 27 - 1 / 36,
            4: 16 / 81 - 1 / 36,
            5: 32 / 243 - 1 / 36,
            6: 64 / 729 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]
    def _roll_bank_or_quit(self):
        # always roll when you have 6 dice to roll
        if self.unbanked_points >= 3000 or self.dice_remaining == 6:
            return "b"
        if not self.dice_remaining or self.dice_remaining == 5:
            return "r"
        roll_tuple = GameLogic.get_scorers(self.last_roll)
        roll = list(roll_tuple)
        abcs = [0, 0, 0, 0, 0, 0]
        # This is the array of how many times the integers 1-6 are represented
        for number in roll:
            abcs[number-1] += 1
            # This is counting how many of each number we have in our array. Number -1 is because our numbers 1-6 are reindexed to 0-5 to to into a list. The location in the array (0-5) are getting added a number of the count.
        if abcs[3] >=3 or abcs[4] >=3 or abcs[5]>=3:
            return "b"
            #If there are triples or more in 4,5,6 bank it
        if GamblingBotThree.chance_to_fail(self.dice_remaining) > 100 / (self.unbanked_points + 1):
            return "b"
        if self.unbanked_points >= 550 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining < 2:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 1:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"
    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    #This is finding out if you have a one essentially as it is looking for one die
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    #This is just checking your different combinations of die
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 500:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        listy_list = [number for number in roll_string]
        if listy_list.count(5)==2 and listy_list.count(1)==0:
            roll_string = ""
            listy_list.remove(5)
            roll_string = "".join(listy_list)
            roll_string += "5"
        self.report("> " + roll_string)
        return roll_string


class BryceTheBrute(BaseBot):
    """Aoife's was working but something broke"""

    def __init__(self):
        from collections import Counter
        self.kept_roll = ()
        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None

    def _roll_bank_or_quit(self):
        """your logic here"""
        if len(self.kept_roll) < 2:
            return "r"
        roll_weight = 0
        bank_weight = 0
        kept_score = GameLogic.calculate_score(self.kept_roll)
        for i in range(300):
            fake_dice = tuple([random.randint(1, 6) for _ in range(6-len(self.kept_roll))])
            fake_roll = GameLogic.get_scorers(self.kept_roll) + fake_dice
            # self.real_print(str(self.kept_roll) + ": self.keptroll. " + str(fake_dice) + ": fake dice. " + str(self.last_roll) + ": self.lastroll")
            # if GameLogic.calculate_score(fake_roll) > self.unbanked_points + 1000:
            #     roll_weight += 3
            fake_score = GameLogic.calculate_score(fake_roll)
            if fake_score > kept_score + 1000:
                # self.real_print("+1.25")
                roll_weight += 1.25
            elif fake_score > kept_score:
                # self.real_print("+1")
                roll_weight += 1
            elif GameLogic.calculate_score(fake_dice) == 0:
                # self.real_print("-3")
                bank_weight += 3
            else:
                # self.real_print("-1")
                bank_weight += 1
        # roll_weight += (2 - len(self.kept_roll)) * 25
        # self.real_print(str(bank_weight) + ": bank weight. " + str(roll_weight) + ": roll weight. " +
        #                 str(self.kept_roll) + ": roll")

        if roll_weight > bank_weight:
            # or len(self.kept_roll) == 1:
            # self.real_print("with a roll of " + str(self.kept_roll) + ", let's roll again")
            return "r"
        else:
            # self.real_print("with a roll of " + str(self.kept_roll) + ", let's bank")
            return "b"

    # self.unbanked_points
    # self.dice_remaining

    # def _this_is_stupid(self, someroll):
    #     roll = GameLogic.get_scorers(someroll)
    #     # if we all dice score, please keep them all
    #     if len(roll) == len(someroll):
    #         # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
    #         return GameLogic.calculate_score(roll)
    #     # lets go for highest average of points per die
    #     highest_score_per_die = 0
    #     highest_scoring_dice = 0
    #     highest_scoring_len = 0
    #     # check each combination of dice, to determine the 'best' value per die, and keep that set
    #     roll = list(roll)
    #     roll.sort()
    #     for i in range(len(roll)):
    #         for j in range(len(roll)):
    #             if len(roll[i: j + 1]):
    #                 test_dice = roll[i: j + 1]
    #                 test_score = GameLogic.calculate_score(roll[i: j + 1]) / len(
    #                     test_dice
    #                 )
    #                 if test_score > highest_score_per_die:
    #                     highest_score_per_die = test_score
    #                     highest_scoring_dice = test_dice
    #                     highest_scoring_len = len(test_dice)
    #                 elif test_score == highest_score_per_die:
    #                     if highest_score_per_die >= 175:
    #                         if len(test_dice) > highest_scoring_len:
    #                             highest_score_per_die = test_score
    #                             highest_scoring_dice = test_dice
    #                             highest_scoring_len = len(test_dice)
    #     return GameLogic.calculate_score(highest_scoring_dice)

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 175:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        self.kept_roll = tuple(highest_scoring_dice)
        self.report("> " + roll_string)
        return roll_string


class CheaterGuy(BaseBot):
    """Aoife's valiant effort to break the game by cracking the random number generator, takes forever"""
    def __init__(self):
        self.cheater = 0
        super().__init__()
        self.kept_dice = ()
        self.done = 0

    def _roll_bank_or_quit(self):
        rc = RandCrack()
        for i in range(624):
            rc.submit(random.getrandbits(32))
        # self.real_print(random.randint(1, 50), rc.predict_randint(1, 50))
        if self.cheater == 1:
            self.cheater = 0
            return "b"
        self.kept_dice = GameLogic.get_scorers(self.last_roll)
        oops = 0
        while oops < 500:
            time.sleep(0.0001)
            if GameLogic.calculate_score(tuple([rc.predict_randint(1, 6) for _ in range(self.dice_remaining)]) + self.kept_dice) > 1000:
                self.cheater = 1
                return "r"
            oops += 1
        return "b"


if __name__ == "__main__":
    num_games = 100

    # NervousNellie.play(num_games)
    # MiddlingMargaret.play(num_games)
    # DaringDarla.play(num_games)
    # YoniBot.play

    print("MarkBot:")
    MarkBot.play(num_games)
    print("\nOur bots:")
    DontFarkleUp.play(num_games)
    GamblingAnonymous.play(num_games)
    GamblingBotThree.play(num_games)
    BryceTheBrute.play(num_games)  # fairly slow, be careful running



