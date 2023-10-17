from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score = {self.points}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)


    def add_points(self):
        self.points += 1
        self.clear()
        self.update_score_board()
