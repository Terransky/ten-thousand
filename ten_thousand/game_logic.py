
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

    @staticmethod  # input: integer between 1 and 6
    def roll_dice(self, dice):
        pass
        # output: tuple with random values between 1 and 6
        # len() of tuple must match len() of input


class Banker:
    """docstring"""

    def __init__(self):
        pass

    def shelf(self):  # input: amount of points(integer) to add to shelf
        pass  # output: no return, temporarily stores unbanked points

    def bank(self):  # takes shelf points and adds to total bank, resets shelf to 0
        pass  # output: sum of bank and shelf

    def clear_shelf(self):  # clear shelf points
        pass









dice_face = { 'one': 0,
             'two': 0,
             'three': 0,
             'four': 0,
             'five': 0,
             'six': 0,
             }
# sides = dice_face.keys()
sides = list(dice_face)

for i in range(6):
    dice_face[random.choice(sides)] += 1

print('one:\t', dice_face['one'])
print('two:\t', dice_face['two'])
print('three:\t', dice_face['three'])
print('four:\t', dice_face['four'])
print('five:\t', dice_face['five'])
print('six:\t', dice_face['six'])
