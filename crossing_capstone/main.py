from turtle import Screen
from util.player import Player
from util.car_manager import CarManager
from util.scoreboard import Scoreboard
import time


def crossing_capstone_game():
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(width=1000, height=600)
    screen.title('Crossing Capstone')
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(player.move_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    screen.exitonclick()


if __name__ == "__main__":
    crossing_capstone_game()
    