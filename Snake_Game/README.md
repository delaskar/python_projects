# **Snake Game**

This is a simple implementation of the classic Snake Game in  <a href="https://www.python.org/downloads/">**Python 3.10**</a>.

## **Installation**

Clone the repository and install the required packages using pip:
```
git clone https://github.com/your-username/snake-game.git
cd snake-game
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
If you are in windows you should install the virtual environment as follows:

`env\Scripts\activate`

## **How to Play**
To start the game, run the file: `run.py` using the following command on the terminal:
```
python run.py
```
Use the ***arrow keys*** to control the snake's direction. The objective is to eat the food without running into the walls or the snake's own tail. The game ends when the snake hits a wall or its own tail.

## **Files**

- ***main.py:*** The main file that runs the game loop.
- ***util/:*** A package containing the classes for the snake, food, and scoreboard.
- ***data.txt:*** A file that stores the high score.
- ***run.py:*** A script to run the game.

**Note:** If tkinter is not working properly, it may need to be installed manually using the command:

```
sudo apt-get install python3-tk
```
