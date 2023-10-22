from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# 1) main screen setup
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
#
# Creating a paddle that responds to keypresses.
screen.tracer(0)
screen.listen()

paddle_right=Paddle((350,0))
paddle_left=Paddle((-350,0))
pong_ball=Ball()
screen.onkey(paddle_right.paddle_up, 'Up')
screen.onkey(paddle_right.paddle_down, 'Down')
screen.onkey(paddle_left.paddle_up, 'w')
screen.onkey(paddle_left.paddle_down, 's')
#

is_on=True
while is_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.move()
    if pong_ball.ycor()>290 or pong_ball.ycor()<-290:
        pong_ball.bounce()

screen.exitonclick()