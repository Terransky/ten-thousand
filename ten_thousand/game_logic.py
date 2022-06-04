
import random
import itertools


class GameLogic:
    """docstring"""

    def __init__(self):
        pass

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

    @staticmethod  # input: tuple of integers that represent six dice roll
    def calculate_score(roll):
        print("calculate score")
        score = 0
        ordered_roll = sorted(roll)
        score_list = [
            (tuple(), 0),
            ((1,), 100),
            ((1, 1), 100),
            ((1, 1, 1), 800),
            ((1, 1, 1, 1), 1000),
            ((1, 1, 1, 1, 1), 1000),
            ((1, 1, 1, 1, 1, 1), 1000),
            ((2,), 0),
            ((2, 2), 0),
            ((2, 2, 2), 200),
            ((2, 2, 2, 2), 200),
            ((2, 2, 2, 2, 2), 200),
            ((2, 2, 2, 2, 2, 2), 200),
            ((3,), 0),
            ((3, 3), 0),
            ((3, 3, 3), 300),
            ((3, 3, 3, 3), 300),
            ((3, 3, 3, 3, 3), 300),
            ((3, 3, 3, 3, 3, 3), 300),
            ((4,), 0),
            ((4, 4), 0),
            ((4, 4, 4), 400),
            ((4, 4, 4, 4), 400),
            ((4, 4, 4, 4, 4), 400),
            ((4, 4, 4, 4, 4, 4), 400),
            ((5,), 50),
            ((5, 5), 50),
            ((5, 5, 5), 400),
            ((5, 5, 5, 5), 500),
            ((5, 5, 5, 5, 5), 500),
            ((5, 5, 5, 5, 5, 5), 500),
            ((6,), 0),
            ((6, 6), 0),
            ((6, 6, 6), 600),
            ((6, 6, 6, 6), 600),
            ((6, 6, 6, 6, 6), 600),
            ((6, 6, 6, 6, 6, 6), 600),
            ((1, 2, 3, 4, 5, 6), 1500),
            ((2, 2, 3, 3, 4, 6), 0),
            ((2, 2, 3, 3, 6, 6), 1500),
            ((1, 1, 1, 2, 2, 2), 0),
        ]
        for potato in score_list:
            if set(potato[0]).issubset(ordered_roll):
                print("found a match! ", potato[0], " found in ", ordered_roll)
                score += potato[1]
                print("roll IS in the score list!", score)
        return "roll is not in score list[0]", score
    # return integer score according to rules of game


if __name__ == "__main__":
    obj = GameLogic
    # print(obj.roll_dice(4))
    # print(obj.roll_dice(6))
    # print(obj.calculate_score((4, 4, 4, 4)))
    print(obj.calculate_score((3,4,3,4,3,4)))

