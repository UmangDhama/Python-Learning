from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle_score=0
        self.paddle2_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.paddle_score,align="center",font=("Courier",50,"normal"))
        self.goto(100, 200)
        self.write(self.paddle2_score, align="center", font=("Courier", 50, "normal"))

    def paddle_point(self):
        self.paddle_score+=1
        self.update_scoreboard()

    def paddle2_point(self):
        self.paddle2_score += 1
        self.update_scoreboard()