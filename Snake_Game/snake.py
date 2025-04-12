from turtle import Turtle
MOVE_DISTANCE=20 #in python, constants are declared with all caps


class Snake:
    def __init__(self):
        self.turtles=[]
        self.create()
        
        
        
    def create(self):
        turtle1 = Turtle(shape='square')
        turtle1.penup()
        turtle1.goto(0, 0)

        turtle2 = Turtle(shape='square')
        turtle2.penup()
        turtle2.goto(-20, 0)

        turtle3 = Turtle(shape='square')
        turtle3.penup()
        turtle3.goto(-40, 0)

        self.turtles = [turtle1, turtle2,turtle3]

    def add_tail(self):
        tail=Turtle(shape='square')
        tail.penup()
        tail.goto(self.turtles[-1].position())
        self.turtles.append(tail)


    def move(self):
        pos=-(len(self.turtles))


        for i in range(-1,pos,-1):
            z = i - 1
            self.turtles[i].goto(self.turtles[z].xcor(), self.turtles[z].ycor())

        self.turtles[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.turtles[0].heading() !=270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)