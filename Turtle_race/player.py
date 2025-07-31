from turtle import Turtle

class PlayTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.color("black")
        self.goto(0, -280)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset_pos(self):
        self.goto(0, -280)
