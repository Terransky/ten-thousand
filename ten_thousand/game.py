try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic
# This takes in both situations of using pytest to run these as modules or running the script locally

game_logic = GameLogic()

class Game:
    intro = """Welcome to Ten Thousand
(y)es to play or (n)o to decline"""

    no = """OK. Maybe another time"""

    # class variables
    die = 6
    round = 1
    score = 0

    def __init__(self) -> None:
        pass



    def play(self, roller=None):
        print(Game.intro)
        usr_input = input("> ").lower()
        if usr_input == "y" or usr_input == "yes":
            #Will need to loop through this line of code somehow

            quit = """Thanks for playing. You earned {} points""".format(Game.score)

            list_of_die = [str(number) for number in game_logic.roll_dice(Game.die)]
            #This is a one line for loop to make all of the numbers from the dice roll (from the game logic function) from the tuple into strings 
            # The gamelogic part of this previous code line is to instantiate a Gamelogic class item from the Gamelogic file, and call the roll_dice method on the number of die we are rolling. 
            # All of this is a really fancy one line map. 
            gambler = ' '.join(list_of_die)

            display = """Starting round {}\nRolling {} dice...""".format(round, Game.die)
            display2 = f"*** {self.rolling()} ***\nEnter dice to keep, or (q)uit:"

            #TO DO NEXT: If roller is not none, then we need to parse the numbers from the text file into the die that are returned. Need to implement this. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
            # numbers = """*** {} ***""".format(gambler)

            # thing_three = """Enter dice to keep, or (q)uit:"""

            # print (display, numbers, thing_three)

            print (display)
            print (display2)

            yes_or_quit = input("> ").lower()
            if yes_or_quit == "q":
                print (quit)
            else:
                pass


        elif usr_input == "n" or usr_input == "no":
            print(Game.no)

    def rolling(self, roller):

        dice = ""
        print(roller)
        if roller:
            dice = "4 4 5 2 3 1"
        else:
            list_of_die = [str(number) for number in game_logic.roll_dice(Game.die)]
            dice = ' '.join(list_of_die)
        print(dice)
        return dice






if __name__ == "__main__":
    new_game = Game()
    new_game.play()
