from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.move()



    def move(self):
        rand_x=random.randint(-280,280)
        rand_y=random.randint(-280,280)
        self.goto(rand_x, rand_y)





