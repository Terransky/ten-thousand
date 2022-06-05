import random

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

    @staticmethod # input: tuple of integers that represent one to six rolled dice
    def calculate_score(dice_roll_tuple):
        dice_roll = list(dice_roll_tuple)
        print(dice_roll)
        score = 0
        #count stores the number of times a specific score has been rolled in the list; for instance, if the 6 dice are rolled an d3 of the faces are 1's, then index 0 of count will be 3.Most references to count will be shifted back by one; ie. to check how many times 4 has been rolled, you look at the (four minus one)th index. This is because you can't roll a 0
        count = [0,0,0,0,0,0]
        #This is the array of how many times the integers 1-6 are represented 

        for roll in dice_roll:
            #Roll corresponds to the value of a single dice roll (integer 1-6)
            #add one to the corresponding place in our "count" array
            count[roll-1] +=1 
            #This is counting how many of each number we have in our array. 


        # We start with seeing if the roll is an edge case and returning the scores if it is one of these

        # If we roll [1, 2, 3, 4, 5, 6] count will be [1,1,1,1,1,1]
        if count == [1,1,1,1,1,1]:
            score +=1500
            print(score)
        
        # If we roll [2,2,3,3,4,6] count will be [0,2,2,1,0,1]
        elif count == [0,2,2,1,0,1]:
            score += 0
            print(score)

        # If we roll [2,2,3,3,4,6] count will be [0,2,2,1,0,1]
        elif count == [0,2,2,1,0,1]:
            score += 0
            print(score)

        # If we roll [2, 2, 3, 3, 6, 6] count will be [0,2,2,0,0,2]
        elif count == [0,2,2,0,0,2]:
            score += 1500
            print(score)
       
       # If we roll [1, 1, 1, 2, 2, 2] count will be [3,3,0,0,0,0]
        elif count == [0,2,2,0,0,2]:
            score += 0
            print(score)

       #This else has the math for the other cases that use math to compute the scores from having multiple things in certain values
        else:
            for face in range (1,7):
                number = count[face-1]
                #The NUMBER of dice with the face value integer we are looking for (aka 4 die that are rolled with 5's faceup)

                if face in range(1,7):
                    if face == 1:
                        if number >=3:
                            #This is if we have three or more die rolled to one
                            score +=(number-2)*1000;
                            print(face, score)
                        else:
                            score +=100*number
                            print(face, score)
                            #This is for one or two die rolled to ones
                    elif face==5:
                        
                        if number >=3:
                            score += (number-2)*500
                            print(face, score)
                            #Three or more die rolled to 5's score 500 each
                        else: 
                            score += 50 * number
                            print(face, score)
                            #One or two die rolled to 5's score 50 each. 
                            
                    else:
                        if number >=3:
                            score += (number-2)*face*100
                            print(face, score)
                        #For other numbers, they only get scores if there are more than three of them rolled. If there are three of these numbers then the score is the face*100*the amount of the number minus two. 
                        
        return score




if __name__ == "__main__":
    obj = GameLogic
    # print(obj.roll_dice(4))
    # print(obj.roll_dice(6))
    print(obj.calculate_score((5,3,6,3,5,3)))
    #print(obj.calculate_score((3,4,3,4,3,4)))
    # (3,3,3,4,4,4) == (3,3,3), (4,4,4)

