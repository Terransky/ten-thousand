

class Game:
    intro = """Welcome to Ten Thousand
(y)es to play or (n)o to decline"""

    no = """OK. Maybe another time"""

    def __init__(self) -> None:
        pass

    def play(self, roller=None):
        print(Game.intro)
        usr_input = input("> ").lower()
        if usr_input == "y" or usr_input == "yes":
            pass
        elif usr_input == "n" or usr_input == "no":
            print(Game.no)


if __name__ == "__main__":
    new_game = Game()
    new_game.play()
