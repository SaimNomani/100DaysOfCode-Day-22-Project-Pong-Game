from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self, player_l, player_r):
        """Take the name of player 1 and player 2."""
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.color("white")
        self.left_score=0
        self.right_score=0
        self.player_left=player_l
        self.player_right=player_r
        self.penup()
        self.display_score()

    def display_score(self):
        """display the scoreboard"""
        self.goto(0,220)
        self.write(f"{self.player_left}\t{self.player_right}\n ",align='center',font=('Courier', 20, 'normal'))
        self.goto(0,200)
        self.write(f"{self.left_score}\t{self.right_score}",align='center',font=('Courier', 30, 'normal'))
    def update_score(self, ball):
        """take the ball as input and update the scoreboard"""
        self.clear()
        if ball.xcor()>380:
            self.left_score+=1
        elif ball.xcor()<-380:
            self.right_score+=1
        self.display_score()
    def get_winner(self):
        "Return the name of the player who has the higher score"
        if self.left_score>self.right_score:
            return self.player_left
        return self.player_right
    def game_over(self):
        """end the game and display the winner"""
        self.goto(0,0)
        self.write(f"Game Over",align='center',font=('Courier', 20, 'normal'))
        self.goto(0,-40)
        self.write(f"{self.get_winner()} wins",align='center',font=('Courier', 20, 'normal'))


