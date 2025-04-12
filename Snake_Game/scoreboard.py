from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f'Your score is: {self.score}',align='center',font=("Courier", 15, "normal"))



    def update(self):
        self.clear()
        self.score+=1
        self.write(f'Your score is: {self.score}', align='center',font=("Courier", 15, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over! Your score is: {self.score}', align='center', font=("Courier", 15, "normal"))

