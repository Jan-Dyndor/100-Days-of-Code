from turtle import Screen
import time
from food import Food
from snake import Snake
from score_board import ScoreBoard


# TODO Crate snake
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
        game_is_on = False
        score_board.game_over()

# Detect collision with tale
    # If the head collides with any of segments in the tail
    #   we have to trigger a game over sequence
    for segment in snake.segments[1:]:
        # Snake_head  is first element, so immediately it return true
        # We can skip that if statement using list slicing!
        # if segment == snake.snake_head:
        #     pass
        # we check first if distance form snake_head (element 0) is less than 10 form segment which is also snake_head
        # (element 0), what results in activation of game over sequence. That is a bug so line above we check if segment
        #  is nake_head and if so, pass and check another segment
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()



screen.exitonclick()
