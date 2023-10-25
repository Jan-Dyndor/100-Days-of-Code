import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import os
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move, "Up")

cars = []
game_is_on = True
make_car = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if make_car % 6 == 0:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move_car()
        # TODO The car object is 20x40, now i measure it like square 20x20. Will try to change it later
        if player.distance(car) < 20:
            print("hit")
            os.system("pause")
    if player.ycor() >= 280:
        player.reset()
        for car in cars:
            pass
            # TODO we need to increment car speed
            # car.move_faster()

    make_car += 1



