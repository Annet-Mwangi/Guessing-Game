import random

class Game:
    def __init__(self, name, min_range, max_range):
        self.name = name
        self.min_range = min_range
        self.max_range = max_range
        self.correct_answer = random.randint(min_range, max_range)
        self.low_messages = [
            "Too low! Try again.",
            "You're getting closer, but still too low.",
            "Almost there, but not quite."
        ]
        self.high_messages = [
            "Too high! Try again.",
            "You're getting closer, but still too high.",
            "Almost there, but not quite."
        ]

    def get_hint(self, guess):
        if guess < self.correct_answer:
            return random.choice(self.low_messages)
        elif guess > self.correct_answer:
            return random.choice(self.high_messages)
        else:
            return "Congratulations! You guessed the number correctly."

    def play(self):
        print(f"Welcome to {self.name}! I'm thinking of a number between {self.min_range} and {self.max_range}.")
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < self.min_range or guess > self.max_range:
                    print("Please enter a number within the specified range.")
                else:
                    hint = self.get_hint(guess)
                    print(hint)
                    if hint.startswith("Congratulations"):
                        break
            except ValueError:
                print("Invalid input. Please enter a number.")