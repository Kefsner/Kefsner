from turtle import Turtle
import random

BALL_MOVE_DISTANCE = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction_list = ["up right", "up left", "down left", "down right"]
        self.direction = ""
        self.reset()

    def move(self):
        if self.direction == "up right":
            self.setpos(self.xcor() + BALL_MOVE_DISTANCE, self.ycor() + BALL_MOVE_DISTANCE)
        elif self.direction == "up left":
            self.setpos(self.xcor() - BALL_MOVE_DISTANCE, self.ycor() + BALL_MOVE_DISTANCE)
        elif self.direction == "down left":
            self.setpos(self.xcor() - BALL_MOVE_DISTANCE, self.ycor() - BALL_MOVE_DISTANCE)
        elif self.direction == "down right":
            self.setpos(self.xcor() + BALL_MOVE_DISTANCE, self.ycor() - BALL_MOVE_DISTANCE)

    def h_bounce(self):
        if self.direction == "up right":
            self.direction = "down right"
        elif self.direction == "up left":
            self.direction = "down left"
        elif self.direction == "down right":
            self.direction = "up right"
        elif self.direction == "down left":
            self.direction = "up left"

    def v_bounce(self):
        if self.direction == "up right":
            self.direction = "up left"
        elif self.direction == "up left":
            self.direction = "up right"
        elif self.direction == "down right":
            self.direction = "down left"
        elif self.direction == "down left":
            self.direction = "down right"

    def reset(self):
        self.direction = random.choice(self.direction_list)
