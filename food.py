from turtle import Turtle
import random

colors = ["red", "white", "yellow", "orange", "pink", "green", "blue"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        color = random.choice(colors)
        self.color(color)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
