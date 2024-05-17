from turtle import Turtle, Screen
import time
from snake import Snake

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)

    snake.move()

scr.exitonclick()
