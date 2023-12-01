from turtle import Screen

from paddle import Paddle
from ball import Ball
from screen import Score
from stage import Stage

import time

screen = Screen()
screen.colormode()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)
screen.listen()


paddle1 = Paddle((-480, 0))
paddle2 = Paddle((480, 0))
ball = Ball()
score = Score()
stage = Stage()

game_is_on = True

# Is a knowing issue that the input does not work for capital W and S.
screen.onkeypress(paddle1.move_up, "w")
screen.onkeypress(paddle1.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")


while game_is_on:
    screen.update()
    time.sleep(.01)
    paddle1.move()
    paddle2.move()
    ball.move()

    if ball.xcor() >= 540:
        score.update_score_p1()
        ball.home()
        ball.reset()

    if ball.xcor() <= -540:
        score.update_score_p2()
        ball.home()
        ball.reset()

    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.h_bounce()

    if ball.xcor() <= -460:
        if paddle1.ycor() - 50 <= ball.ycor() <= paddle1.ycor() + 50:
            ball.v_bounce()

    if ball.xcor() >= 460:
        if paddle2.ycor() - 50 <= ball.ycor() <= paddle2.ycor() + 50:
            ball.v_bounce()

screen.exitonclick()
