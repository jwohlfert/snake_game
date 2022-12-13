from turtle import Turtle
from pathlib import Path
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        if Path("data.txt").is_file():
            with open("data.txt") as f:
                self.high_score = int(f.read())
        else:
            with open("data.txt", "w") as f:
                f.write("0")
            self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
