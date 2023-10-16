from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_seg = Turtle(shape="square")
            snake_seg.color("white")
            snake_seg.penup()
            snake_seg.goto(position)
            self.segments.append(snake_seg)

    def move(self):
        """Move snake forward"""
        for snake_seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[snake_seg - 1].xcor()
            new_y = self.segments[snake_seg - 1].ycor()
            self.segments[snake_seg].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)


