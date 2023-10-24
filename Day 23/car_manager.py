from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.goto(260, random.randint(-250, 250))
        self.seth(180)
        self.shape("square")

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)