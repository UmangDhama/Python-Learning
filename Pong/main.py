from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle=Paddle(350,)
paddle2=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    #Detect collision with r_paddle

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2)<50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect R paddle miss
    if  ball.xcor() > 380 :
        ball.reset_ball()
        scoreboard.paddle2_point()
    #select l paddle miss
    if ball.xcor() < -380 :
        ball.reset_ball()
        scoreboard.paddle_point()

screen.exitonclick()