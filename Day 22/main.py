from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
# TODO Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO PADDLE
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_points()

    # left paddle misses
    if ball.xcor() < -340:
        ball.reset_position()
        score.r_points()







screen.exitonclick()
