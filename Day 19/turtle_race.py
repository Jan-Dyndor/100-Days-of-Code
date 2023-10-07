from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Whithc Turtlle will will a race? Enter a color of a Turtle")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
# tim = Turtle("turtle")
# tim.penup()
# tim.goto(x=-240, y=0)

y = -130
for turtle_number in range(len(colors)):
    name = "tim" + str(turtle_number)
    name = Turtle("turtle")
    name.penup()
    name.color(colors.pop(random.randint(0, len(colors)-1)))
    name.goto(x=-240, y=y)
    y += 50



screen.exitonclick()