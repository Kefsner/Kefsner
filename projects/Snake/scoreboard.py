from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.pencolor("white")

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def save_game(self):
        with open("data", mode="w") as data:
            data.write(str(self.high_score))
