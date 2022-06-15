import sys
from pyparsing import nums


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
        self.random_dice_roll = ""
        #This is the raw random dice roll as a string
        self.random_tuple = ()
        # This is the raw random dice roll as converted to a tuple
        self.chosen_die = []
        # This is the tuple of numbers that the USER chooses to keep from the roll

    # Plan for rewriting the play function:
        # All user entries that are letters should be in one place.
        # Another place should have the flow of the game through rolling dice, validating the results, moving to different rounds etc. Everything is currently mixed up in the play function.

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
            self.new_round(roller)

        elif usr_input == "n" or usr_input == "no":
            print("OK. Maybe another time")
            
    def new_round(self, roller=None):
            self.starting_round(roller)
            self.how_many_dice(roller)
            self.face_up_dice(roller)
            self.gameplay(roller) 

    def gameplay(self, roller=None):
        """This function takes in user inputs. If the user inputs are the letters we handle, we route them to the appropriate cases. Else we route the input to the handle dice selection functions. Whenever we are moving between functions, roller needs to be passed so that if the test files are running, the appropriate responses will be applied from the files to the game."""
        
        in_putty = input("> ").lower()
        usr_input = in_putty.replace(" ", "")
        # We are taking in the lower case of the input and removing spaces! Advanced test 3 is looking for no spaces!
        
        if usr_input == "b" or usr_input == "bank":
            self.bank(roller)
        elif usr_input == "r" or usr_input == "roll":
            self.roll_again(roller, usr_input)
        elif usr_input == "q" or usr_input == "quit":
            self.end_game()
        elif self.banker.balance >= 10000:
            print("You Won The Game!!!!!!!!!")
            self.end_game()
        else:
            #This is the case where integers are entered
            
            self.chosen_die += (tuple(int(num) for num in usr_input))
            # print(self.chosen_die)

            self.pumpkin_eater(roller)
            
            
    

    def starting_round(self, roller):
        """This method tells the user which round they are in."""
        print(f"Starting round {self.round}")

    def how_many_dice(self, roller):
        """
        This method displays how many dice you are rolling.
        """
        print(f"Rolling {self.die} dice...")


    def face_up_dice(self, roller):
        """
        This method rolls the dice and displays the rolled dice face values.
        """
        self.random_dice_roll = self.rolling_dice(roller)
        

        if self.game_logic.winner_winner(self.random_tuple)==True:
            self.chosen_die = ()
            #This resets the chosen_die tuple whenever we get new die or there is an invalid user input.
            print(f"*** {self.random_dice_roll} ***\nEnter dice to keep, or (q)uit:")
        else:
            print(f"*** {self.random_dice_roll} ***")
            self.zilch(roller)
            #When we roll the dice, we will check whether there is a possible score or not.
        

    
    def pumpkin_eater(self, roller=None):
        """This method validates whether the dice the user wants to keep are valid"""
        # CURRENT ISSUES: The validate function as written currently is having trouble with more numbers entered than the roll has if the numbers are repeats of the same digit.

        
        if self.game_logic.validate_keepers(self.random_tuple, tuple(self.chosen_die)) is False:
            self.chosen_die =()
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {self.random_dice_roll} ***\nEnter dice to keep, or (q)uit:")
            self.gameplay(roller)

        else:
            self.shelf(roller)


    def shelf(self, roller = None):
        """
        This method keeps track of the scores in the shelf.
        """
        
        self.banker.shelf(self.game_logic.calculate_score(self.chosen_die))
        
        self.die -= len(self.chosen_die)
        
        print(
            f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
        self.gameplay(roller)


    def bank(self, roller=None):
        """
        This method banks the score, clears the shelf and ends the current round.
        """
        print(f"You banked {self.banker.shelved} points in round {self.round}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        self.round += 1
        self.die = 6
        self.new_round(roller)


    def rolling_dice(self, roller=None) -> str:
        """
        This method rolls the dice and returns a STRING of the random dice face values
        """
        rolls_royce = roller or self.game_logic.roll_dice
        
        list_of_die = rolls_royce(self.die)

        self.random_dice_roll = ' '.join([str(number) for number in list_of_die])
        #This is the raw random dice roll as a string
        self.random_tuple = tuple(list_of_die)
        # THis is the tuple of the dice rolled 
        
        return self.random_dice_roll

    def roll_again(self, roller, usr_input):
        """
        This method allows the user to roll the dice again in the current round of game.
        """
        if self.die == 0:
            self.die = 6
        #This is the functionality for hot dice

        self.how_many_dice(roller)
        self.face_up_dice(roller)
        self.gameplay(roller)
        
            
    def zilch(self, roller=None):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        self.banker.shelved = 0
        self.bank(roller)

        # When we write the winner_winner method in GameLogic we can call this function.

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit(1)


    def interruption(self):
        print(f"Thanks for playing. The game has crashed due to a bug! You earned {self.banker.balance} points")

    def keyboard_quit(self, message):
        sys.exit(message)


if __name__ == "__main__":
    try:
        new_game = Game()
        new_game.play()
    except KeyboardInterrupt:
        new_game.keyboard_quit('You have pressed CTRL-C so Goodbye!')
