from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.setheading(180)
    tim.forward(10)
def move_counter_clockwise():
    tim.left(10)
    tim.forward(10)
def move_clockwise():
    tim.right(10)
    tim.forward(10)

def Clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="space", fun=Clear_screen)
screen.exitonclick()
