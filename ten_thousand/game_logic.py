
import random
import itertools


class GameLogic:
    """docstring"""

    def __init__(self):
        pass

    @staticmethod  # input: tuple of integers that represent six dice roll
    def calculate_score(self, roll):
        pass
        # return integer score according to rules of game

    @staticmethod  # input: integer between 1 and 6, representing number of die
    def roll_dice(dice):

        if 1 <= dice <= 6:

            dice_rack = []

            for i in range(dice):
                dice_value = random.randint(1, 6)
                dice_rack.append(dice_value)
            dice_tuple = tuple(dice_rack)
            return dice_tuple

        # output: tuple with random values between 1 and 6, representing fresh rolls
        # len() of tuple must match len() of input


if __name__ == "__main__":

    obj = GameLogic
    print(obj.roll_dice(4))
    print(obj.roll_dice(6))

