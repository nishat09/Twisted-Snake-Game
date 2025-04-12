from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
from hawk import Hawk


screen=Screen()
food=Food()
score=Score()
hawk = Hawk()

screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor('Blue')

snake=Snake()
screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')





# turtle1=Turtle(shape='square')
# turtle1.penup()
# turtle1.goto(0,0)
#
# turtle2=Turtle(shape='square')
# turtle2.penup()
# turtle2.goto(-20,0)
#
# turtle3=Turtle(shape='square')
# turtle3.penup()
# turtle3.goto(-40,0)

# turtles=[turtle1,turtle2,turtle3]
screen.update()

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    hawk.chase(snake.turtles[0])

    if snake.turtles[0].distance(food) < 15:
        food.move()
        score.update()
        snake.add_tail()

    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-280 or snake.turtles[0].ycor()>280 or snake.turtles[0].ycor()<-280:
        game_on=False
        score.game_over()

    head=snake.turtles[0]


    for i in snake.turtles:
        if i==head:
            pass
        else:
            if head.distance(i)<10:
                game_on = False
                score.game_over()

    if hawk.distance(snake.turtles[0]) < 15:
        game_on = False
        score.game_over()

screen.exitonclick()