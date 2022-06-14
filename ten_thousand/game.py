import sys
from pyparsing import nums


try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic

class Game:

    @staticmethod
    def zilch():
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

    def __init__(self) -> None:
        self.die = 6
        self.round = 1
        self.game_logic = GameLogic()
        self.banker = Banker()
        self.nums = ""
        self.zilch = None
        self.usr_input = None

    def play(self, roller=None):
            """
            This method displays welcome message the terminal and initiates the game.
            """
            print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
            self.usr_input = input("> ").lower()
            while self.usr_input != 'y' and self.usr_input != 'yes' and self.usr_input != "n" and self.usr_input != "no":
                print("Invalid response")
                self.usr_input = input("> ").lower()
            if self.usr_input == "y" or self.usr_input == "yes":
                while True:
                    self.zilch = None
                    print(f"Starting round {self.round}")
                    self.rolled_dice(roller)
                    if self.zilch:
                        self.usr_input = input("> ").lower()
                    else:
                        self.usr_input = "b"
                    if self.usr_input[0] in self.nums:
                        self.shelf()
                    if self.usr_input == "b" or self.usr_input == "bank":
                        self.bank()
                    if self.usr_input == "r" or self.usr_input == "roll":
                        self.roll_again(roller)
                    if self.usr_input == "q" or self.usr_input == "quit":
                        break
                    if self.banker.balance >= 10000:
                        break
                self.end_game()
            elif self.usr_input == "n" or self.usr_input == "no":
                print( "OK. Maybe another time")

    def rolled_dice(self, roller):
        """
        This method displays the rolled dice.
        """
        self.nums = self.rolling_dice(roller)
        print(f"Rolling {self.die} dice...\n*** {self.nums} ***")
        self.nums_int = tuple([int(num) for num in self.nums.split(" ")])
        self.zilch = self.game_logic.calculate_score(self.nums_int)
        if self.zilch == 0:
            Game.zilch()
            self.banker.clear_shelf()
        if self.zilch != 0:
            print("Enter dice to keep, or (q)uit:")


    def shelf(self):
        """
        This method keeps track of the dice and scores in the shelf.
        """
        if self.usr_input != "q" or self.usr_input != "quit":
            nums_tuple = tuple([int(num) for num in self.nums.split()])
            keep_nums = [int(num) for num in self.usr_input if num != "q" and num != " "]
            sanitized_keep_nums = list(nums_tuple)
            self.cheater(keep_nums, sanitized_keep_nums, nums_tuple, sanitized_keep_nums)
            self.usr_input = input("> ").lower()
        else:
            self.end_game()

    def cheater(self, keep_nums, r_dice, nums_tuple, sanitized_keep_nums):
        """
        This methods validates the user input and prevents players from cheating
        """
        message = ""
        self.usr_input = ""
        while message is not None: 
            message = None
            self.usr_input = ""
            for x in keep_nums:
                if keep_nums.count(x) > r_dice.count(x):
                    message = "Cheater!!! Or possibly made a typo..."         
            if message:
                print(message)
                print(f"*** {self.nums} ***\nEnter dice to keep, or (q)uit:")
                self.usr_input = input("> ").lower()       
            else:
                break
            if self.usr_input == "q" or self.usr_input == "quit":
                self.end_game()
            else:
                keep_nums = [int(num) for num in self.usr_input if num != " "]
                r_dice = list(nums_tuple)
                sanitized_keep_nums_1 = []
                for x in keep_nums:
                    if x in sanitized_keep_nums:
                        sanitized_keep_nums_1.append(x)
                        sanitized_keep_nums.remove(x)
        self.die -= len(keep_nums)
        self.banker.shelf(self.game_logic.calculate_score(keep_nums))
        print(f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
        if self.die == 0:
            self.die = 6 


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

    def roll_again(self, roller):
        """
        This method allows the user to roll the dice again in the current round of game.
        """
        while self.usr_input != "b" or self.usr_input != "bank" or self.usr_input != "q" or self.usr_input != "quit":
            self.rolled_dice(roller)
            if self.zilch != 0:
                self.usr_input = input("> ").lower()
                self.shelf()
            else:
                self.usr_input = "b"
            if self.usr_input == "b":
                self.bank()
                break
            if self.usr_input == "q":
                self.end_game()
                break
            if self.die <= 0:
                self.bank()
                break

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit(1)

    def interruption(self):
        sys.exit(f"Thanks for playing. The game has crashed due to a bug! You earned {self.banker.balance} points")


if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except KeyboardInterrupt:
        new_game.interruption()


import sys
from pyparsing import nums


try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic

class Game:

    @staticmethod
    def zilch():
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

    def __init__(self) -> None:
        self.die = 6
        self.round = 1
        self.game_logic = GameLogic()
        self.banker = Banker()
        self.nums = ""
        self.zilch = None

    def play(self, roller=None):
            """
            This method displays welcome message the terminal and initiates the game.
            """
            print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
            self.usr_input = input("> ").lower()
            while self.usr_input != 'y' and self.usr_input != 'yes' and self.usr_input != "n" and self.usr_input != "no":
                print("Invalid response")
                self.usr_input = input("> ").lower()
            if self.usr_input == "y" or self.usr_input == "yes":
                while True:
                    self.zilch = None
                    print(f"Starting round {self.round}")
                    self.rolled_dice(roller)
                    if self.zilch:
                        self.usr_input = input("> ").lower()
                    else:
                        self.usr_input = "b"
                    if self.usr_input[0] in self.nums:
                        self.shelf()
                        self.usr_input = input("> ").lower()
                    if self.usr_input == "b" or self.usr_input == "bank":
                        self.bank()
                    if self.usr_input == "r" or self.usr_input == "roll":
                        self.roll_again(roller)
                    if self.usr_input == "q" or self.usr_input == "quit":
                        break
                    if self.banker.balance >= 10000:
                        break
                self.end_game()
            elif self.usr_input == "n" or self.usr_input == "no":
                print( "OK. Maybe another time")

    def rolled_dice(self, roller):
        """
        This method displays the rolled dice.
        """
        self.nums = self.rolling_dice(roller)
        print(f"Rolling {self.die} dice...\n*** {self.nums} ***")
        self.nums_int = tuple([int(num) for num in self.nums.split(" ")])
        self.zilch = self.game_logic.calculate_score(self.nums_int)
        if self.zilch == 0:
            Game.zilch()
            self.banker.clear_shelf()
        if self.zilch != 0:
            print("Enter dice to keep, or (q)uit:")


    def shelf(self):
        """
        This method keeps track of the dice and scores in the shelf.
        """
        if self.usr_input != "q" or self.usr_input != "quit":
            nums_tuple = tuple([int(num) for num in self.nums.split()])
            keep_nums = [int(num) for num in self.usr_input if num != "q" and num != " "]
            sanitized_keep_nums = list(nums_tuple)
            self.cheater(keep_nums, sanitized_keep_nums, nums_tuple, sanitized_keep_nums )
        else:
            self.end_game()

    def cheater(self, keep_nums, r_dice, nums_tuple, sanitized_keep_nums):
        """
        This methods validates the user input and prevents players from cheating
        """
        message = ""
        self.usr_input = ""
        while message is not None: 
            message = None
            self.usr_input = ""
            for x in keep_nums:
                if keep_nums.count(x) > r_dice.count(x):
                    message = "Cheater!!! Or possibly made a typo..."         
            if message:
                print(message)
                print(f"*** {self.nums} ***\nEnter dice to keep, or (q)uit:")
                self.usr_input = input("> ").lower()       
            else:
                break
            if self.usr_input == "q" or self.usr_input == "quit":
                self.end_game()
            else:
                keep_nums = [int(num) for num in self.usr_input if num != " "]
                r_dice = list(nums_tuple)
                sanitized_keep_nums_1 = []
                for x in keep_nums:
                    if x in sanitized_keep_nums:
                        sanitized_keep_nums_1.append(x)
                        sanitized_keep_nums.remove(x)
        self.die -= len(keep_nums)
        self.banker.shelf(self.game_logic.calculate_score(keep_nums))
        print(f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")

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

    def roll_again(self, roller):
        """
        This method allows the user to roll the dice again in the current round of game.
        """
        while self.usr_input != "b" or self.usr_input != "bank" or self.usr_input != "q" or self.usr_input != "quit":
            self.rolled_dice(roller)
            if self.zilch != 0:
                self.usr_input = input("> ").lower()
                self.shelf()
            else:
                self.usr_input = "b"
            if self.usr_input == "b":
                self.bank()
                break
            if self.usr_input == "q":
                self.end_game()
                break
            if self.die <= 0:
                self.bank()
                break

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit(1)

    def interruption(self):
        sys.exit(f"Thanks for playing. The game has crashed due to a bug! You earned {self.banker.balance} points")


if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except KeyboardInterrupt:
        new_game.interruption()


