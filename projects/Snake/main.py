from turtle import Screen
from move import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scoreboard.update_score()

screen.listen()


screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


def reset():
    scoreboard.reset()
    scoreboard.update_score()
    snake.reset()
    scoreboard.save_game()


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food.xcor(), food.ycor()) < 10:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.add_segment()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        reset()
    if snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            reset()

screen.exitonclick()
