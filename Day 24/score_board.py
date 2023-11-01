from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = self.read_data_file()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > int(self.high_score):
            self.high_score = self.points
        self.points = 0
        self.update_score_board()

    def add_points(self):
        self.points += 1
        self.update_score_board()

    def write_data_file(self):
        with open("data.txt", mode="w") as data_file:
            data_file.write(str(self.high_score))

    def read_data_file(self):
        with open("data.txt", "r") as data_file:
            score = data_file.read()
            return score
