from turtle import Turtle

class Hawk(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(200, 200)  # Start position (can change)

    def chase(self, target):
        """Chase the target (snake head)"""
        self.setheading(self.towards(target))  # Face the snake's head
        self.forward(10)  # Move toward it
