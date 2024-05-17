from turtle import Turtle, Screen

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for positions in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(positions)


scr.exitonclick()