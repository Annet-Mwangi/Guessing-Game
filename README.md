Guessing Game
A simple number guessing game with SQLite database integration for tracking game results.
Description
This Guessing Game is a Python application that challenges players to guess a randomly generated number within a specified range. The game provides hints to guide the player towards the correct answer and keeps track of the number of attempts. Game results are stored in a SQLite database using SQLAlchemy ORM.
Features

Customizable number range for each game
Hint system (too high/too low)
Player name input
Game results stored in SQLite database
Leaderboard showing top 5 results

Requirements

Python 3.6+
SQLAlchemy

Installation

Clone this repository or download the source code.
Install the required dependencies:
Copypip install sqlalchemy


Usage

Run the script:
Copypython guessing_game.py

Follow the on-screen prompts to:

Enter your name
Set the minimum and maximum numbers for the range
Start guessing the number


After each game, you'll see the leaderboard and have the option to play again.

Database
The game uses a SQLite database named guessing_game.db to store game results. The database is automatically created in the same directory as the script when you run the game for the first time.
Contributing
Contributions to improve the game are welcome. Please feel free to submit a Pull Request.
License
This project is open source and available under the MIT License.