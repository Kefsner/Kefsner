from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setposition(-250, 260)
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)

    def limit_lines(self):
        self.setposition(-300, -260)
        self.pendown()
        self.setposition(300, -260)
        self.penup()
        self.setposition(-300, 260)
        self.pendown()
        self.setposition(300, 260)
        self.penup()

    def add(self):
        self.score += 1
        self.clear()
        self.setposition(-250, 260)
        self.write(f"Score: {self.score}", font=FONT)
        self.limit_lines()
