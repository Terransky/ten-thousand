
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
        self.keep_nums = []
        self.sanitized_keep_nums = []
        self.nums_tuple = ()
        self.nums = ""

    def play(self, roller=None):
        """
        This method displays welcome message the terminal and initiates the game.
        Two out of four tests passed.
        The function is incomplete
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
                print(f"Starting round {self.round}\nRolling {self.die} dice...")
                self.nums = self.rolling(roller)
                print(f"*** {self.nums} ***\nEnter dice to keep, or (q)uit:")
                usr_input = input("> ").lower()
                if usr_input[0] in self.nums:
                    self.unbanked(usr_input)
                    usr_input = input("> ").lower()
                if usr_input == "b" or usr_input == "bank":
                    self.bank()
                if usr_input == "r" or usr_input == "roll":
                    while usr_input != "b" or usr_input != "bank" or usr_input != "q" or usr_input != "quit":
                        self.nums = self.rolling(roller)
                        print(f"Rolling {self.die} dice...*** {self.nums} ***\nEnter dice to keep, or (q)uit:")
                        usr_input = input("> ").lower()
                        self.unbanked(usr_input, roller)
                        usr_input = input("> ").lower()
                        if usr_input == "b":
                            self.bank()
                            break
                        if self.die <= 0:
                            self.bank()
                            break
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

    def unbanked(self, usr_input):
        self.nums_tuple = tuple([int(num) for num in self.nums.split()])
        self.keep_nums = [int(num) for num in usr_input]
        self.sanitized_keep_nums = [x for x in self.keep_nums if x in self.nums_tuple]
        self.banker.shelf(self.game_logic.calculate_score(self.sanitized_keep_nums))
        self.die -= len(self.sanitized_keep_nums)
        print(f"You have {self.banker.shelved} unbanked points and {self.die} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")

    def bank(self):
        print(f"You banked {self.banker.shelved} points in round {self.round}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        self.round += 1
        self.die = 6

    def rolling(self, roller):
        list_of_die = []
        if roller:
            list_of_die = [str(number)
                for number in roller(self.die)]
        else:
            list_of_die = [str(number)
                for number in self.game_logic.roll_dice(self.die)]
        return ' '.join(list_of_die)

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

if __name__ == "__main__":
    new_game = Game()
    new_game.play()
