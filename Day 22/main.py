from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
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



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()




screen.exitonclick()
