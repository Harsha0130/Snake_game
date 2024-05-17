from turtle import Turtle, Screen
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for positions in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    # 1st segment goto new segment, 2nd to 1st, and 3rd to 2nd
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

scr.exitonclick()
