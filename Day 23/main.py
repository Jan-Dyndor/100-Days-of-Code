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
level = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if make_car % 6 == 0:
        car = CarManager()
        cars.append(car)
        # make_car += 1
    for car in cars:
        car.move_car()
        # TODO The car object is 20x40, now i measure it like square 20x20. Will try to change it later
        if player.distance(car) < 20:
            print("hit")
            os.system("pause")
    if player.ycor() >= 280:
        car_temp = CarManager()
        car_temp.move_faster()
        cars.append(car_temp)
        for car in cars:
            car.clear()
            car.hideturtle()
        player.reset()
        cars.clear()
        car_temp.clear()
        level += 1
    make_car += 1



