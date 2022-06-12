import sys

from pyparsing import nums

# This takes in both situations of using pytest to run these as modules or running the script locally

try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic

class Game:
    def __init__(self) -> None:
        self.die = 6
        self.round = 1
        self.game_logic = GameLogic()
        self.banker = Banker()
        self.nums = ""
        self.dice_tuple = None  # keeps dice tuple for future comparisons

    def play(self, roller=None):
        """
        This method displays welcome message the terminal and initiates the game.
        """
        print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
        usr_input = input("> ").lower()
        while usr_input != 'y' and usr_input != 'yes' and usr_input != "n" and usr_input != "no":
            print("Invalid response")
            usr_input = input("> ").lower()

        if usr_input == "y" or usr_input == "yes":
            # Will need to loop through this line of code somehow
            while True:
                # This is a one line for loop to make all of the numbers from the dice roll (from the game logic
                # function) from the tuple into strings The gamelogic part of this previous code line is to
                # instantiate a Gamelogic class item from the Gamelogic file, and call the roll_dice method on the
                # number of die we are rolling. All of this is a really fancy one line map.
                print(f"Starting round {self.round}")
                usr_input = self.gameplay(roller)
                if usr_input == "q" or usr_input == "quit":
                    break
                if self.banker.balance >= 10000:
                    break
            # TO DO NEXT: If roller is not none, then we need to parse the numbers from the text file into the die
            # that are returned. Need to implement this. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # thing_three = """Enter dice to keep, or (q)uit:""" print (display, numbers, thing_three)
            self.end_game()
        elif usr_input == "n" or usr_input == "no":
            print("OK. Maybe another time")

    def gameplay(self, roller):
        self.rolled_dice(roller)
        usr_input = input("> ").lower()
        if usr_input[0] in self.nums:
            # print("this should NOT say Q: " + usr_input + " IF IT SAYS Q SOMETHING IS WRONG")
            self.shelf(usr_input)
            if self.die == 0:
                self.die = 6
                # self.hot_dice(roller)
            usr_input = input("> ").lower()

        if usr_input == "b" or usr_input == "bank":
            self.bank()
        if usr_input == "r" or usr_input == "roll":
            # print("ROLL AGAIN WAS CALLED FROM GAMEPLAY USR_INPUT = R: " + usr_input)
            self.roll_again(roller, usr_input)
        return usr_input

    def rolled_dice(self, roller):
        """
        This method displays the rolled dice.
        """
        dice_tuple = self.dice_tuple
        self.nums = self.rolling_dice(roller)
        print(f"Rolling {self.die} dice...\n*** {self.nums} ***")
        potato = [int(x) for x in self.nums.split(" ")]
        if self.game_logic.calculate_score(potato) == 0:  # calculates held dice score
            self.zilch()  # prints zilch statement
            self.banker.shelved = 0
            self.bank()  # updates round and balance
            # print("ROLL AGAIN WAS CALLED FROM ROLLED DICE")
            self.roll_again()  # continues game to next round in play function

        else:
            print(f"Enter dice to keep, or (q)uit:")

    def shelf(self, usr_input):
        """
        This method keeps track of the dice and scores in the shelf.
        """
        nums_tuple = tuple([int(num) for num in self.nums.split()])
        keep_nums = [int(num) for num in usr_input]
        sanitized_keep_nums = [x for x in keep_nums if x in nums_tuple]
        # sanitized_keep_nums = list(nums_tuple)
        # j = list(nums_tuple)
        # sanitized_keep_nums_1 = []
        # for x in keep_nums:
        #     if x in sanitized_keep_nums:
        #         sanitized_keep_nums_1.append(x)
        #         sanitized_keep_nums.remove(x)
        # message = None
        # for x in keep_nums:
        #     if keep_nums.count(x) > j.count(x):
        #         message = "cheater or typo"
        # if message: print(message)

        self.banker.shelf(self.game_logic.calculate_score(sanitized_keep_nums))
        self.die -= len(sanitized_keep_nums)
        print(
            f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")

    def bank(self):
        """
        This method banks the score, clears the shelf and ends the current round.
        """
        print(f"You banked {self.banker.shelved} points in round {self.round}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        self.round += 1
        self.die = 6

    def rolling_dice(self, roller) -> str:
        """
        This method rolls the dice.
        """
        if roller:
            int_list_of_die = roller(self.die)
        else:
            int_list_of_die = self.game_logic.roll_dice(self.die)
        return ' '.join([str(number) for number in int_list_of_die])

    def roll_again(self, roller=None, usr_input="b"):
        """
        This method allows the user to roll the dice again in the current round of game.
        """
        while usr_input != "b" or usr_input != "bank" or usr_input != "q" or usr_input != "quit":
            self.rolled_dice(roller)
            usr_input = input("> ").lower()
            if usr_input[0] in self.nums:
                # print("this should NOT say Q: " + usr_input + " IF IT SAYS Q SOMETHING IS WRONG")
                self.shelf(usr_input)
                if self.die == 0:
                    self.die = 6
                    # self.hot_dice(roller)
                usr_input = input("> ").lower()

            if usr_input == "b":
                self.bank()
                break
            if usr_input == "q":
                self.end_game()
                break
            if self.die <= 0:
                self.die = 6
                break

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

    def interruption(self):
        print(f"Thanks for playing. The game has crashed due to a bug! You earned {self.banker.balance} points")

    # def hot_dice(self, roller):
    #     # self.gameplay(roller)
    #     pass

    @staticmethod
    def zilch():
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")


if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except Exception as e:
        print(f"ERROR: {e}")
        new_game.interruption()