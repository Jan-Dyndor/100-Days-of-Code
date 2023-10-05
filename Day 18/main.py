import math
import random
from turtle import Turtle, Screen
from random import randrange
# Timmy = Turtle()
# screen = Screen()
# Timmy.shape("turtle")
#
# # Timmy.pencolor((0.01,0.02,0.33))
# # Drow a Square
# # turn = 4
# # while turn > 0 :
# #     Timmy.forward(100)
# #     Timmy.right(90)
# #     turn -= 1
# #
# #  Drow a dashed line 10 on 10
# # for _ in range(10):
# #     Timmy.color("black")
# #     Timmy.forward(10)
# #     Timmy.penup()
# #     Timmy.forward(10)
# #     Timmy.pendown()
# #     Timmy.forward(10)
#
#
#
#
# # Challange 3
def change_color():
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

#
# # triangle
# # Timmy.pencolor(change_color())
# # turn = 3
# # while turn > 0:
# #     Timmy.forward(100)
# #     Timmy.right(120)
# #     turn -= 1
# # # Square
# # turn = 4
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.forward(100)
# #     Timmy.right(90)
# #     turn -= 1
# # Timmy.forward(100)
# # # Pentagon
# # turn = 5
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(72)
# #     Timmy.forward(100)
# #     turn -= 1
# # # hexagon
# # turn = 6
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(60)
# #     Timmy.forward(100)
# #     turn -= 1
# # # heptagon
# # turn = 7
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(51.43)
# #     Timmy.forward(100)
# #     turn -= 1
# # # octagon
# # turn = 8
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(45)
# #     Timmy.forward(100)
# #     turn -= 1
# # # nonanon
# # turn = 9
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(40)
# #     Timmy.forward(100)
# #     turn -= 1
# # # decaonon
# # turn = 10
# # Timmy.pencolor(change_color())
# # while turn > 0:
# #     Timmy.right(36)
# #     Timmy.forward(100)
# #     turn -= 1
#
# # Refactored version
# # def drow(num_of_sides):
# #     angle = 360 / num_of_sides
# #     for _ in range(num_of_sides):
# #         Timmy.forward(100)
# #         Timmy.right(angle)
# #
# #
# # for turns in range(3,11):
# #     Timmy.pencolor(change_color())
# #     drow(turns)
#
#
# # Random Walk
# # TODO 1. Tickness of a line, speed tutrtle
# def forward():
#     Timmy.forward(30)
#
#
# def backward():
#     Timmy.backward(30)
#
#
# def right():
#     Timmy.right(90)
#
#
# def left():
#     Timmy.left(90)
#
#
# list_of_functions = [forward,backward,right,left]
# go = 2000
# Timmy.width(10)
# Timmy.speed(10)
# while go > 0:
#     Timmy.pencolor(change_color())
#     random_function = random.choice(list_of_functions)
#     random_function()
#     go -= 1
#
#
# # Draw a Spirograph
# Timmy.speed(100)
# # def draw_spin(gap):
# #     circles =0
# #     turns = math.floor(360 /gap)
# #     for _ in range(turns):
# #         Timmy.pencolor(change_color())
# #         Timmy.circle(100)
# #         Timmy.right(gap)
# #         circles +=1
# #     print(circles)
# # draw_spin(5)
#
# screen.exitonclick()
#
#
