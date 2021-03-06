import random
from collections import Counter

class GameLogic:
    """docstring"""
    """docstring_test"""

    def __init__(self):
        pass

    @staticmethod  # input: integer between 1 and 6, representing number of die
    def roll_dice(dice):
        """
        This method returns a tuple of randomly generated dice set.
        The used a module called random to generate six random numbers from 1 to 6.
        """

        if 1 <= dice <= 6:

            dice_rack = []

            for i in range(dice):
                dice_value = random.randint(1, 6)
                dice_rack.append(dice_value)
            dice_tuple = tuple(dice_rack)
            return dice_tuple

        # output: tuple with random values between 1 and 6, representing fresh rolls
        # len() of tuple must match len() of input

    @staticmethod  # input: tuple of integers that represent one to six rolled dice
    def calculate_score(dice_roll_tuple):
        """
        This method calculates the score of the player per the dice 10,000 rulebook. 
        We used nested if/else statements to account for different configurations/combinations of dice set.
        """
        dice_roll = list(dice_roll_tuple)
        score = 0
        # count stores the number of times a specific score has been rolled in the list; for instance, if the 6 dice
        # are rolled an d3 of the faces are 1's, then index 0 of count will be 3.Most references to count will be
        # shifted back by one; ie. to check how many times 4 has been rolled, you look at the (four minus one)th
        # index. This is because you can't roll a 0
        count = [0, 0, 0, 0, 0, 0]
        # This is the array of how many times the integers 1-6 are represented

        for roll in dice_roll:
            # Roll corresponds to the value of a single dice roll (integer 1-6)
            # add one to the corresponding place in our "count" array
            count[roll-1] += 1
            # This is counting how many of each number we have in our array.

        # We start with seeing if the roll is an edge case and returning the scores if it is one of these

        # If we roll [1, 2, 3, 4, 5, 6] count will be [1,1,1,1,1,1]
        if count == [1, 1, 1, 1, 1, 1]:
            score += 1500

        # If we roll [2,2,3,3,4,6] count will be [0,2,2,1,0,1]
        elif count == [0, 2, 2, 1, 0, 1]:
            score += 0

        # If we roll [2,2,3,3,4,6] count will be [0,2,2,1,0,1]
        elif count == [0, 2, 2, 1, 0, 1]:
            score += 0

        # If we roll [2, 2, 3, 3, 6, 6] count will be [0,2,2,0,0,2]
        # the first count is the LIST count,
        # with the formatted dice rolls as explained above. The `.count()` part is a builtin python function that
        # shows how many times an integer appears in an array. This statement just checks if the user has any 3 pairs
        # of dice.
        elif count.count(2) == 3:
            score += 1500

        # If we roll [1, 1, 1, 2, 2, 2] count will be [3,3,0,0,0,0]
        # We're not sure if this is supposed to be a special
        # case for ALL rolls which have two triples, or if this was just an example that is scored as normally
        # according to the other rules. If it's the former, then use basically the same syntax as the doubles checker
        # above. For now we're leaving it how it is because we're not sure what to do with it.
        elif count == [3, 3, 0, 0, 0, 0]:
            score += 1200

        # This else has the math for the other cases that use math to compute the scores from having multiple things
        # in certain values
        else:
            for face in range(1, 7):
                number = count[face-1]
                # The NUMBER of dice with the face value integer we are looking for (aka 4 die that are rolled with
                # 5's faceup)

                if face in range(1, 7):
                    if face == 1:
                        if number >= 3:
                            # This is if we have three or more die rolled to one
                            score += (number-2)*1000

                        else:
                            score += 100*number

                            # This is for one or two die rolled to ones
                    elif face == 5:

                        if number >= 3:
                            score += (number-2)*500

                            # Three or more die rolled to 5's score 500 each
                        else:
                            score += 50 * number

                            # One or two die rolled to 5's score 50 each.

                    else:
                        if number >= 3:
                            score += (number-2)*face*100

                        # For other numbers, they only get scores if there are more than three of them rolled. If there are three of these numbers then the score is the face*100*the amount of the number minus two.

        return score

    @staticmethod
    def how_many(souffle):
        """This function is doing the count functionality from the calculate_score. It takes in a tuple (called souffle), turns it into a list(called listerine), and counts how many times each of the values from 1-6 are represented(the count list is renamed abcs)."""
        listerine = list(souffle)
        abcs = [0, 0, 0, 0, 0, 0]
        # This is the array of how many times the integers 1-6 are represented

        for number in listerine:
            abcs[number-1] += 1
            # This is counting how many of each number we have in our array. Number -1 is because our numbers 1-6 are reindexed to 0-5 to to into a list. The location in the array (0-5) are getting added a number of the count. 
        return abcs


    @staticmethod
    def get_scorers(roll):
        roll_points = Counter(roll)
        if (len(roll_points) == 3 and list(roll_points.values()) == [2, 2, 2]) or (len(roll_points) == 6):
            return roll

        output = []
        for dice in roll_points:
            number_of_occurrences = roll_points[dice]
            if (dice == 1 or dice == 5) or number_of_occurrences >= 3:
                output += [dice] * number_of_occurrences

        return tuple(output)

    def validate_keepers(roll, keepers):
        abcroll = GameLogic.how_many(roll)
        abckeepers = GameLogic.how_many(keepers)
        if abcroll>abckeepers:
            
            if all (number in roll for number in keepers): 
                return True
        else:
            return False

if __name__ == "__main__":
    game_logic = GameLogic()
    print(game_logic.calculate_score((2,2,2,2)))