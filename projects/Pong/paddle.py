from turtle import Turtle

MOVE_DISTANCE = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setpos(position)

    def move(self):
        if self.ycor() == 260 and self.heading() == 90:
            pass
        elif self.ycor() == -260 and self.heading() == 270:
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def move_up(self):
        self.setheading(90)

    def move_down(self):
        self.setheading(-90)
