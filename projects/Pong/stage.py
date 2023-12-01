from turtle import Turtle


class Stage(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("White")
        self.penup()
        self.setpos(-500, -310)
        self.pendown()
        self.setpos(500, -310)
        self.penup()
        self.setpos(-500, 310)
        self.pendown()
        self.setpos(500, 310)
        self.penup()
        self.setpos(0, 310)
        self.pendown()
        self.setpos(0, -310)
        self.penup()
        self.setpos(0, -50)
        self.pendown()
        self.circle(50)