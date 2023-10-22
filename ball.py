from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speed(1)
        self.goto(0,0)
        self.y_movement = 10
        self.x_movement = 10
        self.ball_move_speed=0.1
    def move(self):
        new_x=self.xcor()+self.x_movement
        new_y=self.ycor()+self.y_movement
        self.goto(new_x, new_y)
    def bounce_y(self):
        """ball bounces back from the top and bottom walls."""
        self.y_movement *= -1
    def bounce_x(self):
        """ball bounces back off the paddles."""
        self.ball_move_speed*=0.9
        self.x_movement *= -1
    def reset(self):
        """Reset the ball after a paddle misses."""
        self.ball_move_speed=0.1
        self.goto(0,0)
        self.bounce_x()





