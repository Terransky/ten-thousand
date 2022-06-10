
try:
    from ten_thousand.banker import Banker
    from ten_thousand.game_logic import GameLogic
except:
    from banker import Banker
    from game_logic import GameLogic


# This takes in both situations of using pytest to run these as modules or running the script locally




class Game:
    intro = """Welcome to Ten Thousand
(y)es to play or (n)o to decline"""

    no = """OK. Maybe another time"""

    def __init__(self) -> None:
        self.die = 6
        self.round = 1
        self.game_logic = GameLogic()
        self.banker = Banker()

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
                quit = f"Thanks for playing. You earned {self.banker.balance} points"
            # This is a one line for loop to make all of the numbers from the dice roll (from the game logic function) from the tuple into strings
            # The gamelogic part of this previous code line is to instantiate a Gamelogic class item from the Gamelogic file, and call the roll_dice method on the number of die we are rolling.
            # All of this is a really fancy one line map.
                display = f"Starting round {self.round}\nRolling {self.die} dice..."
                nums = self.rolling(roller)
                display2 = f"*** {nums} ***\nEnter dice to keep, or (q)uit:"
                nums_tuple = tuple([int(num) for num in nums.split()])
                print(display)
                print(display2)
                usr_input = input("> ").lower()
                if usr_input[0] in nums:
                    keep_nums = [int(num) for num in usr_input]
                    sanitized_keep_nums = [x for x in keep_nums if x in nums_tuple]
                    self.banker.shelf(self.game_logic.calculate_score(sanitized_keep_nums))
                    self.die -= len(sanitized_keep_nums)
                    display3 = f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:"
                    print(display3)
                    usr_input = input("> ").lower()
                if usr_input == "b" or usr_input == "bank":
                    display4 = f"You banked {self.banker.shelved} points in round {self.round}"
                    self.banker.bank()
                    display5 = f"Total score is {self.banker.balance} points"
                    print(display4)
                    print(display5)
                    self.round += 1
                    self.die = 6
                if usr_input == "r" or usr_input == "roll":
                    nums = self.rolling(roller)
                    display7 = f"Rolling {self.die} dice...\n*** {nums} ***\nEnter dice to keep, or (q)uit:"
                    print(display7)
                    usr_input = input("> ").lower()
                if usr_input == "q" or usr_input == "quit":
                    break

            # TO DO NEXT: If roller is not none, then we need to parse the numbers from the text file into the die that are returned. Need to implement this. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # thing_three = """Enter dice to keep, or (q)uit:"""

            # print (display, numbers, thing_three)

            display6 = f"Thanks for playing. You earned {self.banker.balance} points"
            print(display6)
        elif usr_input == "n" or usr_input == "no":
            print(Game.no)

    def rolling(self, roller):
        list_of_die = []
        if roller:
            list_of_die = [str(number)
                           for number in roller(self.die)]
        else:
            list_of_die = [str(number)
                           for number in self.game_logic.roll_dice(self.die)]
        return ' '.join(list_of_die)


if __name__ == "__main__":
    new_game = Game()
    new_game.play()
