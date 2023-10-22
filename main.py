from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# main screen setup
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
#
screen.tracer(0)
#
# taking name of players as screen input
player_1=screen.textinput(title="player 1",prompt="enter name of player 1" )
player_2=screen.textinput(title="player 2",prompt="enter name of player 2" )
#
# creating score_board object and passes name players as argumnet
score_board=Scoreboard(player_l=player_1, player_r=player_2)
#
# Creating a paddle that responds to keypresses.
paddle_right=Paddle((350,0))
paddle_left=Paddle((-350,0))
screen.listen()
screen.onkey(paddle_right.paddle_up, 'Up')
screen.onkey(paddle_right.paddle_down, 'Down')
screen.onkey(paddle_left.paddle_up, 'w')
screen.onkey(paddle_left.paddle_down, 's')
#
# creating a pong ball object
pong_ball=Ball()
#
is_on=True
while is_on:
    time.sleep(pong_ball.ball_move_speed)
    screen.update()
    pong_ball.move()
    # detect collision with top and bottom walls
    if pong_ball.ycor()>285 or pong_ball.ycor()<-285:
        pong_ball.bounce_y()
    # detect collision with paddles and bounce back
    if (pong_ball.distance(paddle_right)<60 and pong_ball.xcor()>320) or (pong_ball.distance(paddle_left)<60 and pong_ball.xcor()< -320):
        pong_ball.bounce_x()
    # detect if any paddle misses the ball
    if pong_ball.xcor()<-380:
        score_board.update_score(pong_ball)
        pong_ball.reset()
    elif pong_ball.xcor()>380:
        score_board.update_score(pong_ball)
        pong_ball.reset()
    # game over
    if score_board.left_score>4 or score_board.right_score>4:
        score_board.game_over()
        is_on=False

screen.exitonclick()