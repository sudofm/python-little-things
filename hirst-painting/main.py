import turtle as t
from turtle import Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('damien-hirst.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
colors_list = [(225, 230, 227), (210, 154, 107), (221, 204, 123), (142, 86, 65), (210, 93, 71), (149, 160, 183), (123, 81, 93)]
mam = t.Turtle()
mam.speed("fastest")
mam.penup()
mam.hideturtle()
mam.setheading(225)
mam.forward(350)
mam.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    mam.dot(20, random.choice(colors_list))
    mam.forward(50)
    if dot_count % 10 == 0:
        mam.setheading(90)
        mam.forward(50)
        mam.setheading(180)
        mam.forward(500)
        mam.setheading(0)

screen = Screen()
screen.exitonclick()