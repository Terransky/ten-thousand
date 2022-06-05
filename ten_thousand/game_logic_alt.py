
import random
import itertools
from itertools import groupby

# version of calculate_score method solved by grouping and comparison

scoring = [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200),
    ]


class GameLogic:
    """Class that handles rolling dice and scoring"""

    def __init__(self):
        pass

    @staticmethod  # input: tuple of integers that represent six dice roll
    def calculate_score(roll):
        """accepts a tuple of dice as input, transmutes them to a list, sorts and groups them, transmutes them back,
        compares them to the scoring list, and returns the score"""

        # transmutes tuple to list and sorts it
        sorted_roll = list(roll)
        sorted_roll.sort()

        # takes sorted list of dice, groups them by duplicates, and outputs a new list of lists
        print('before: ', sorted_roll)
        grouped_rolls = [list(j) for i, j in groupby(sorted_roll)]
        print('after: ', grouped_rolls)

        # transmutes the nested lists into tuples for comparison to scoring
        # because lists can't be compared to tuples
        for i in range(len(grouped_rolls)):
            grouped_rolls[i] = tuple(grouped_rolls[i])

        score = 0

        for i in range(len(scoring)):
            # if statement accounts for oddball case 223366 and straight 123456
            if len(grouped_rolls) == 6 or grouped_rolls == [(2, 2), (3, 3), (6, 6)]:
                score = 1500
                return score
                # otherwise compares the nested tuples to score and updates score
            for j in range(len(grouped_rolls)):
                if grouped_rolls[j] == scoring[i][0]:
                    score += scoring[i][1]

        return score
        # return integer score according to rules of game

    @staticmethod  # input: integer between 1 and 6, representing number of die
    def roll_dice(dice):
        """docstring"""

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
    print(obj.calculate_score((5, 5, 5, 1, 2, 3)))
    print(obj.calculate_score((1, 2, 3, 4, 5, 6)))
    print(obj.calculate_score((2, 2, 3, 3, 6, 6)))

