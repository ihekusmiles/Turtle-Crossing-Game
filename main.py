import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen parameters
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# Create objects from classes
player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Increase level, car's speed, and have turtle reset position
    if player.is_at_finished_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.clear()
        scoreboard.increase_level()

screen.exitonclick()


