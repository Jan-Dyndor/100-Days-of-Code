from turtle import Turtle, Screen
from random import randrange
Timmy = Turtle()
screen = Screen()
Timmy.shape("turtle")

# Timmy.pencolor((0.01,0.02,0.33))
# Drow a Square
# turn = 4
# while turn > 0 :
#     Timmy.forward(100)
#     Timmy.right(90)
#     turn -= 1
#
#  Drow a dashed line 10 on 10
# for _ in range(10):
#     Timmy.color("black")
#     Timmy.forward(10)
#     Timmy.penup()
#     Timmy.forward(10)
#     Timmy.pendown()
#     Timmy.forward(10)




# Challange 3
def change_color():
    r = randrange(0,255,10)
    g = randrange(0,255,10)
    b = randrange(0,255,10)
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


# triangle
Timmy.pencolor(change_color())
turn = 3
while turn > 0:
    Timmy.forward(100)
    Timmy.right(120)
    turn -= 1
# Square
turn = 4
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.forward(100)
    Timmy.right(90)
    turn -= 1
Timmy.forward(100)
# Pentagon
turn = 5
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(72)
    Timmy.forward(100)
    turn -= 1
# hexagon
turn = 6
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(60)
    Timmy.forward(100)
    turn -= 1
# heptagon
turn = 7
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(51.43)
    Timmy.forward(100)
    turn -= 1
# octagon
turn = 8
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(45)
    Timmy.forward(100)
    turn -= 1
# nonanon
turn = 9
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(40)
    Timmy.forward(100)
    turn -= 1
# decaonon
turn = 10
Timmy.pencolor(change_color())
while turn > 0:
    Timmy.right(36)
    Timmy.forward(100)
    turn -= 1




screen.exitonclick()

