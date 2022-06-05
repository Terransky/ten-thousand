
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

    @staticmethod
    def checkScore(dice_roll_tuple):
        dice_roll = list(dice_roll_tuple)
        print(dice_roll)
        score = 0
        #count stores the number of times a specific score has been rolled in the list; for instance, if the 6 dice are rolled an d3 of the faces are 1's, then index 0 of count will be 3.Most references to count will be shifted back by one; ie. to check how many times 4 has been rolled, you look at the (four minus one)th index. This is because you can't roll a 0
        count = [0,0,0,0,0,0]
        #This is the array of how many times the integers 1-6 are represented 

        for roll in dice_roll:
            #Roll corresponds to the calue of a single dice roll (integer 1-6)
            #add one to the corresponding place in our "count" array
            count[roll-1] +=1 
            #This is counting how many of each number we have in our array. 

        for face in range (1,7):
            number = number
            #This is for possible dice values of 1-6
            if face in range(1,7):
                if face == 1:
                    if number >=3:
                        #i-1 is the position of the integer we are looking for in the count array wince we set our range as 1-6 but the array counts as 1-5
                        score +=(number-2)*1000;
                        #We have the minus two here because the first two (ie. if you get a pair of numbers) we do not care about the scores.
                    else:
                        score +=100*number
                if face==5:
                    if number >=3:
                        score += (number-2)*500
                    else: score += 50 * number
                else:
                    if number >=3:
                        score += number*face*100
                    



    @staticmethod  # input: tuple of integers that represent one to six rolled dice
    def calculate_score(roll):
        print("calculate score")
        
        score_list = [
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
        score_list1 = [
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
        # This score list is amended from the one in the test. In the for loop, we are adding the new value to the existing sum. Thus if we have 5 2's, it will add the scores for having 1, 2, 3, 4, and 5, 2's. Thus we have amended the scores so that when everything is added up we get the expected value for the scores. 
       
        score = 0
        ordered_roll = sorted(roll)

        def checkScore(roll)

        # for potato in score_list1:
        #     #Here potato in scorelist is saying score list at i. i is potato or the place in the score list as we iterate through it.
        #     if set(potato[0]).issubset(ordered_roll):
        #         #Here we are checking if the from ordered roll is in any of the full lines in the line in the sorted list (which we have assigned to the variable potato)
        #         print("found a match! ", potato[0], " found in ", potato[1])
        #         score += potato[1]
        # return score

    # return integer score according to rules of game

        # for potato in range(len(score_list)):
        #     if sorted_roll == score_list[potato][0]:
        #         score = score_list[potato][1]
        #         print(sorted_roll)
        #         print(score_list[i][1])

    #TODO - We need to split up the roll tuple we get to look for multiple tuples in the score array.

#Using the collection - we could count the amount of numbers in the roll that we take in, take the most common of the sorted data, and then compare THOSE TUPLES with the items in the list most common in the scores list or some other way to compare





if __name__ == "__main__":
    obj = GameLogic
    # print(obj.roll_dice(4))
    # print(obj.roll_dice(6))
    print(obj.calculate_score((5,)))
    #print(obj.calculate_score((3,4,3,4,3,4)))
    # (3,3,3,4,4,4) == (3,3,3), (4,4,4)

