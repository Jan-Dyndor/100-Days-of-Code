from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LIST = list()


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(260, random.randint(-250, 250))
        self.seth(180)
        self.shape("square")
        CAR_LIST.append(self)

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def move_faster(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def reset_cars(self):
        self.reset()

