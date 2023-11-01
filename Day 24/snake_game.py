from turtle import Screen
import time
from food import Food
from snake import Snake
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")

screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO Move snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


#   Collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.add_points()
#     Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score_board.write_data_file()
        score_board.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score_board.write_data_file()
            score_board.reset()
            snake.reset()




screen.exitonclick()
