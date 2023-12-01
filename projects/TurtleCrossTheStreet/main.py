import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

scoreboard = Scoreboard()
scoreboard.limit_lines()

cars = []
new_car = 0

screen.onkeypress(player.move, "Up")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    if new_car >= 6 / (scoreboard.score + 1):
        cars.append(CarManager())
        new_car = 0
    else:
        new_car += 1

    if player.ycor() >= FINISH_LINE_Y:
        player.reset()
        scoreboard.add()

    for n in range(len(cars)):
        cars[n].move(scoreboard.score)
        if cars[n].xcor() - 20 <= player.xcor() <= cars[n].xcor() + 20:
            if cars[n].ycor() - 10 <= player.ycor() <= cars[n].ycor() + 10:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()
