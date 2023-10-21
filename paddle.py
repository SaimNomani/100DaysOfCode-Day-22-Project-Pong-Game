from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_position):
        """Create a paddle at the provided paddle position."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(paddle_position)

    def paddle_down(self):
        """Move the paddle downwards"""
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)

    def paddle_up(self):
        """Move the paddle upwards"""
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

