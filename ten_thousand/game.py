
from hashlib import new
import sys

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
        self.current_score = 0

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

    
    def rolling_dice(self, roller)  -> str:
        # This arrow function is saying our *return* value will be a data-type check. If we are returning something that is not a string, the program will catch it before it runs. 
        """
        This method rolls the dice and returns the actual numbers on the dice as a string.
        """
        if roller:
            int_list_of_die = roller(self.die)
        else:
            int_list_of_die = self.game_logic.roll_dice(self.die)
        return ' '.join([str(number) for number in int_list_of_die])


    def rolled_dice(self, roller):
        """
        This method displays the rolled dice. We are using this method to calculate the score of the returned dice and determine whether the user has zilch points or whether they can choose to shelve points from certain dice.
        """
        self.nums = self.rolling_dice(roller)
        self.nums = self.nums.split(" ")
        print(self.nums)
        

        print(f"Rolling {self.die} dice...\n*** {self.nums} ***")
        if self.current_score==0:
            self.zilch()
            
        else:
            print("Enter dice to keep, or (q)uit:")
            

    def shelf(self, usr_input):
        """
        This method keeps track of the dice and scores in the shelf. This is where the user chooses dice to shelve
        """
        nums_tuple = tuple([int(num) for num in self.nums.split()])
        keep_nums = [int(num) for num in usr_input]
        sanitized_keep_nums = [x for x in keep_nums if x in nums_tuple]
        self.current_score = self.game_logic.calculate_score(sanitized_keep_nums)
        self.banker.shelf(self.current_score)
        self.die -= len(sanitized_keep_nums)
        print(f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")

    def bank(self):
        """
        This method banks the score, clears the shelf and ends the current round. This is the function we are saying will create a new round and a new round score of 0 (clearing the shelf).
        """
        if self.current_score == 0:
            print(f"You banked 0 points in round {self.round}")        

        else:
            print(f"You banked {self.banker.shelved} points in round {self.round}")
        
        self.banker.bank()
        # This takes shelf points and adds to total bank, resets shelf to 0
        print(f"Total score is {self.banker.balance} points")

        self.round += 1
        self.die = 6
        #What this is doing here with the round and the die is starting a new round. 

    
    def zilch(self):
        """This method returns a custom comment if the dice roll does not include any scoring die."""
        # self.current_score()
        
        self.bank()        
        self.banker.clear_shelf()
        # if self.current_score == 0:
            
        print("****************************************\n**        Zilch!!! Round over         **\n****************************************")


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
            if self.die <= 0:
                print("You're out of die")
                self.bank()
                break   


    def end_game(self):
        sys.exit(f"\nThanks for playing. You earned {self.banker.balance} points")

if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except KeyboardInterrupt:
        new_game.end_game()
