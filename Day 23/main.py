import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import os
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()

screen.listen()
screen.onkey(player.move, "Up")

cars = []
game_is_on = True
make_car = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Create a car every 6 loops
    if make_car % 6 == 0:
        car = CarManager()
        cars.append(car)
    # move every car
    for car in cars:
        car.move_car()
        # detect a collision with a car
        if player.distance(car) < 20:
            score.game_over()
            screen.update()
            os.system("pause")
    # Player wins
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
        score.next_level()
    make_car += 1
