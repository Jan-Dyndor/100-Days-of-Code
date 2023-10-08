from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Whithc Turtlle will will a race? Enter a color of a Turtle")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
all_turtle = []

is_race_on = False
y = -130
for turtle_number in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors.pop(random.randint(0, len(colors)-1)))
    new_turtle.goto(x=-240, y=y)
    y += 50
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You have WON! The {winning_color} turtle was the fastest!")
            else:
                print(f"You LOSE! The {winning_color} turtle was the fastest!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
