
# from game_logic import GameLogic

class Banker:
    """Shelves and banks points"""

    def __init__(self, balance=0, shelved=0):
        # balance is total, shelf is temporary round score
        self.balance = balance
        self.shelved = shelved



    def shelf(self, shelf_points):  # input: amount of points(integer) to add to shelf
        self.shelved = shelf_points
        # output: no return, temporarily stores unbanked points

    def bank(self):  # takes shelf points and adds to total bank, resets shelf to 0
        self.balance += self.shelved
        self.shelved = 0
        return self.balance
        # output: return sum of bank and shelf

    def clear_shelf(self):  # clear shelf points
        self.shelved = 0



if __name__ == "__main__":
    pass
