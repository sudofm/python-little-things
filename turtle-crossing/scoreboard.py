from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-240, 250)
        self.update_level_display()
        self.hideturtle()

    def update_level_display(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level = self.level + 1
        self.clear()
        self.update_level_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
