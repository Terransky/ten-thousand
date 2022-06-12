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
            # This is a one line for loop to make all of the numbers from the dice roll (from the game logic function) from the tuple into strings
            # The gamelogic part of this previous code line is to instantiate a Gamelogic class item from the Gamelogic file, and call the roll_dice method on the number of die we are rolling.
            # All of this is a really fancy one line map.
                print(f"Starting round {self.round}")
                self.rolled_dice(roller)
                usr_input = input("> ").lower()
                if usr_input[0] in self.nums:
                    self.shelf(usr_input)
                    usr_input = input("> ").lower()
                if usr_input == "b" or usr_input == "bank":
                    self.bank()
                if usr_input == "r" or usr_input == "roll":
                    self.roll_again(roller, usr_input)
                if usr_input == "q" or usr_input == "quit":
                    break
                if self.banker.balance >= 10000:
                    break
            # TO DO NEXT: If roller is not none, then we need to parse the numbers from the text file into the die that are returned. Need to implement this. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # thing_three = """Enter dice to keep, or (q)uit:"""
            # print (display, numbers, thing_three)
            self.end_game()
        elif usr_input == "n" or usr_input == "no":
            print( "OK. Maybe another time")

    def rolled_dice(self, roller):
        """
        This method displays the rolled dice.
        """
        self.nums = self.rolling_dice(roller)
        print(f"Rolling {self.die} dice...\n*** {self.nums} ***\nEnter dice to keep, or (q)uit:")

    def shelf(self, usr_input):
        """
        This method keeps track of the dice and scores in the shelf.
        """
        nums_tuple = tuple([int(num) for num in self.nums.split()])
        keep_nums = [int(num) for num in usr_input]
        sanitized_keep_nums = list(nums_tuple)
        j = list(nums_tuple)
        sanitized_keep_nums_1 = []
        for x in keep_nums:
            if x in sanitized_keep_nums:
                sanitized_keep_nums_1.append(x)
                sanitized_keep_nums.remove(x)
        self.cheater(keep_nums, j, self.die)

    def cheater(self, keep_nums, j, die):
        message = ""
        sanitized_keep_nums_1 = []
        sanitized_keep_nums = []
        usr_input = ""
        while message is not None: 
            message = None
            usr_input = ""
            for x in keep_nums:
                if keep_nums.count(x) > j.count(x):
                    message = "Cheater!!! Or possibly made a typo..."         
            if message:
                print(message)
                print(f"*** {self.nums} ***\nEnter dice to keep, or (q)uit:")
                usr_input = input("> ").lower()       
            else:
                break
            nums_tuple = tuple([int(num) for num in self.nums.split()])
            keep_nums = [int(num) for num in usr_input.split()]
            sanitized_keep_nums = list(nums_tuple)
            j = list(nums_tuple)
            sanitized_keep_nums_1 = []
            for x in keep_nums:
                if x in sanitized_keep_nums:
                    sanitized_keep_nums_1.append(x)
                    sanitized_keep_nums.remove(x)
        die -= len(sanitized_keep_nums_1)
        self.die = die
        self.banker.shelf(self.game_logic.calculate_score(sanitized_keep_nums_1))
        print(f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank "
              f"your points or (q)uit:")
    
    def bank(self):
        """
        This method banks the score, clears the shelf and ends the current round.
        """
        print(f"You banked {self.banker.shelved} points in round {self.round}")
        if self.die >= 1:
            self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        self.round += 1
        self.die = 6

    def rolling_dice(self, roller)  -> str:
        """
        This method rolls the dice.
        """
        if roller:
            int_list_of_die = roller(self.die)
        else:
            int_list_of_die = self.game_logic.roll_dice(self.die)
        return ' '.join([str(number) for number in int_list_of_die])
    
    def roll_again(self, roller, usr_input):
        """
        This method allows the user to roll the dice again in the current round of game.
        """
        while usr_input != "b" or usr_input != "bank" or usr_input != "q" or usr_input != "quit":
            self.rolled_dice(roller)
            usr_input = input("> ").lower()
            self.shelf(usr_input)
            usr_input = input("> ").lower()
            if usr_input == "b":
                self.bank()
                break
            if usr_input == "q":
                self.end_game()
                break

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

    def interruption(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")


if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except:
        new_game.interruption()

