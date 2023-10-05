#  Firstly we have to install a package of colorgram
# import colorgram
# colors = colorgram.extract("color_image.jpg", 50)
# colors_list_rgb = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     colors_list_rgb.append((r, g, b))
# print(colors_list_rgb)
import random
import turtle

list_colors = [(237, 244, 250), (32, 107, 148), (224, 154, 87), (213, 131, 158), (6, 52, 93), (118, 172, 194),
               (34, 132, 81), (148, 80, 31), (19, 169, 203), (207, 156, 18), (229, 210, 103), (138, 25, 44),
               (210, 90, 121), (141, 183, 166), (10, 100, 57), (13, 64, 126), (222, 213, 7), (11, 44, 35), (81, 81, 20),
               (224, 169, 192), (58, 51, 11), (138, 61, 85), (3, 89, 115), (168, 207, 187), (240, 171, 155),
               (72, 157, 107), (157, 25, 16), (215, 96, 57), (148, 211, 223), (87, 24, 58), (167, 194, 220),
               (95, 125, 176)]
#  TODO 10 on 10 painting, r = 20, space between dots = 50

# from turtle import Turtle, Screen
import turtle as t
t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
screen = t.Screen()

def draw_painting(circle_size, space_between_dots):
    tim.penup()
    tim.setposition(-150, -200)
    tim.pendown()
    for _ in range(100):
        for _ in range(10):
            tim.pencolor(random.choice(list_colors))
            tim.dot(circle_size)
            tim.penup()
            tim.forward(space_between_dots)
        possition = tim.pos()
        tim.setposition(-150,possition[1]+space_between_dots)
        tim.seth(0)

draw_painting(20,50)





















screen.exitonclick()