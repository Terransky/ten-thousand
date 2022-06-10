
try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic


# This takes in both situations of using pytest to run these as modules or running the script locally

game_logic = GameLogic()
banker = Banker()


class Game:
    intro = """Welcome to Ten Thousand
(y)es to play or (n)o to decline"""

    no = """OK. Maybe another time"""

    die = 6

    round = 1

    def __init__(self) -> None:
        pass

    def play(self, roller=None):
        """
        This method displays welcome message the terminal and initiates the game.
        Two out of four tests passed.
        The function is incomplete
        """
        print(Game.intro)
        usr_input = input("> ").lower()
        if usr_input == "y" or usr_input == "yes":
            # Will need to loop through this line of code somehow
            while True:
                quit = f"Thanks for playing. You earned {banker.balance} points"
            # This is a one line for loop to make all of the numbers from the dice roll (from the game logic
                # function) from the tuple into strings The gamelogic part of this previous code line is to
                # instantiate a Gamelogic class item from the Gamelogic file, and call the roll_dice method on the
                # number of die we are rolling. All of this is a really fancy one line map.
                display = f"Starting round {Game.round}\nRolling {Game.die} dice..."
                nums = self.rolling(roller)
                display2 = f"*** {nums} ***\nEnter dice to keep, or (q)uit:"
                nums_tuple = tuple([int(num) for num in nums.split()])
                banker.shelf(game_logic.calculate_score(nums_tuple))
                print(display)
                print(display2)
                usr_input = input("> ").lower()
                game_logic.calculate_score(nums_tuple)
                if usr_input[0] in nums:
                    # Clean usr_input from a string to a list of ints that we can work with easily.
                    keep_nums = [int(num) for num in usr_input]
                    # Make sure that all the selected nums are actually in the list of rolled nums TODO: Handle edge
                    #  cases better (ie. don't just ignore bad user inputs, tell the user they're bad.) for now we're
                    #  just ignoring them
                    sanitized_keep_nums = [x for x in keep_nums if x in nums_tuple]
                    banker.shelf(game_logic.calculate_score(sanitized_keep_nums))
                    Game.die -= len(sanitized_keep_nums)
                    display3 = f"You have {banker.shelved} unbanked points and {Game.die} dice remaining\n(r)oll " \
                               f"again, (b)ank your points or (q)uit: "
                    print(display3)
                    usr_input = input("> ").lower()
                    # You banked 50 points in round 1
                    # Total score is 50 points
                if usr_input == "q" or usr_input == "quit":
                    break
                if usr_input == "b" or usr_input == "bank":
                    display4 = f"You banked {banker.shelved} points in round {Game.round}"
                    display5 = f"Total score is {banker.shelved} points"
                    print(display4)
                    print(display5)
                    banker.bank()
                    Game.round += 1
                    Game.die = 6
                if usr_input == "r" or usr_input == "roll":
                    self.rolling()

            # TO DO NEXT: If roller is not none, then we need to parse the numbers from the text file into the die
            # that are returned. Need to implement this. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # thing_three = """Enter dice to keep, or (q)uit:"""

            # print (display, numbers, thing_three)

            display6 = f"Thanks for playing. You earned {banker.balance} points"
            print(display6)
        elif usr_input == "n" or usr_input == "no":
            print(Game.no)

    def rolling(self, roller):
        dice = ""
        list_of_die = []
        if roller:
            # Because of flo.py, roller already returns the list of numbers defined in the text file.
            list_of_die = [str(number)
                           for number in roller(6)]
        else:
            # in the case that roller isn't defined, roll the dice randomly as normal.
            list_of_die = [str(number)
                           for number in game_logic.roll_dice(Game.die)]
        return ' '.join(list_of_die)


if __name__ == "__main__":
    new_game = Game()
    new_game.play()
