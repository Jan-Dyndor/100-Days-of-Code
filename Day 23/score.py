from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level:{self.level}", align="center", font=("Curier", 20, "normal"))

    def next_level(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Curier", 30, "normal"))
