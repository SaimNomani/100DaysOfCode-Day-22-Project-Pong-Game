from turtle import Turtle, Screen

# 1) main screen setup
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
#
# Creating a paddle that responds to keypresses.
screen.tracer(0)
screen.listen()
def down():
    new_ycor=paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_ycor)
def up():
        new_ycor = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_ycor)
paddle=Turtle("square")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
# 

is_on=True
while is_on:
    screen.update()

screen.exitonclick()