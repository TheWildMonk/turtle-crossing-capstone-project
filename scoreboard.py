from turtle import Turtle

FONT = ("raleway", 16, "bold")
LEVEL = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.color("#009432")
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.color("#EA2027")
        self.penup()
        self.hideturtle()
        self.home()
        self.write("GAME OVER!", align="center", font=FONT)
