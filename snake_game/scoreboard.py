from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.write(f"Score = {self.score}", font=("Arial", 24, "normal"), align="center")

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)







