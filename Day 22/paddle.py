from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddles(position)


    def create_paddles(self, position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


