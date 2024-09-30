from games import Game

class GuessingGameCLI:
    def __init__(self):
        self.games = {
            1: Game("Dragon's Den", 1, 3),
            2: Game("Treasure Hunt", 1, 4),
            3: Game("Mystery Mansion", 1, 10),
            4: Game("Pirate's Plunder", 1, 5)
        }

    def play(self):
        while True:
            print("Choose a game:")
            for key, game in self.games.items():
                print(f"{key}. {game.name}")
            try:
                choice = int(input("Enter the game number: "))
                if choice in self.games:
                    self.games[choice].play()
                else:
                    print("Invalid game number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")