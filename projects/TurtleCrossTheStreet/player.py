from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def reset(self):
        self.setposition(STARTING_POSITION)

