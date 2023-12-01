from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.pencolor("white")
        self.sety(330)
        self.write(f"{self.score_p1} vs {self.score_p2}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.write(f"{self.score_p1} vs {self.score_p2}", align=ALIGNMENT, font=FONT)

    def update_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.write(f"{self.score_p1} vs {self.score_p2}", align=ALIGNMENT, font=FONT)

