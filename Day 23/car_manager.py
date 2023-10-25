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
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(260, random.randint(-250, 250))
        self.seth(180)
        self.shape("square")
        self.move_increment = 10
        self.starting_distance = 5



    def move_car(self):
        self.forward(self.starting_distance)
        print(self.starting_distance)
        self.starting_distance += self.move_increment
        print(self.starting_distance)

    def hit(self):
        """ Will return True if player collided with car"""

    # def move_faster(self):
    #     self.new_distance += MOVE_INCREMENT
    #     self.forward(self.new_distance)
    #     print(self.new_distance)
    #


