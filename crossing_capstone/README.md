# **Crossing Capstone**

This project is a game made using Python and the Turtle graphics library. The goal of the game is to safely cross a busy street, avoiding cars.

## **Installation**

To run this game, you must have a **Python 3.10** and the Turtle graphics library installed on your computer. If you do not have these installed, you can download from the official <a href="https://www.python.org/downloads/">Python website</a>.

***NOTE:*** The turtle module is installed by default in python

Once you have Python, you can run the game by running the run.py file in your terminal:

`python3 run.py`

## **Usage**
When you run the game, a new window will appear showing the game board. You can move the player using the arrow key: **↑** (Up)  on your keyboard. The goal of the game is to safely cross the street and Every time you complete a crossing the cars start moving faster.

If you get hit by a car, the game will end and your score will be displayed. You can run the play again or quit the game.

## **Files**
The project contains the following files:

- **main.py:** The main file for the game logic.
- **run.py:** A file to run the game.
- **util/:** A directory containing utility files for the game.

The **util**/ directory contains the following files:

- **__ init __.py:** An empty file to indicate that the directory is a Python package.
- **car_manager.py:** A file containing the logic for generating and moving cars on the game board.
- **player.py:** A file containing the logic for the player character.
- **scoreboard.py:** A file containing the logic for displaying the player's score.
