from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speed(1)
        self.goto(0,0)
        self.x_movement=10
        self.y_movement=10
    def move(self):
        new_x=self.xcor()+self.x_movement
        new_y=self.ycor()+self.y_movement
        self.goto(new_x, new_y)
    def bounce(self):
        self.y_movement*=-1



