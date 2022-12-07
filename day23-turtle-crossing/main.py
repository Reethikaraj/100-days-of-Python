import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# player
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
# Car
car_manager = CarManager()
# Scoreboard
scoreboard = Scoreboard()
# Game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            time.sleep(1)
            game_is_on = False
    # Reached finish line
    if player.is_at_finish_line():
        scoreboard.clear()
        scoreboard.increase_level()
        player.goto_start()
        car_manager.increase_speed()

