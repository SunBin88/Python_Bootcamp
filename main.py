from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


# create objects of each class and setup each of them
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


ball = Ball()

# ready to listen the key
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect the collision with
    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.hit()

    if ball.xcor() > 385 or ball.xcor() < -385:
        game_is_on = False





screen.exitonclick()