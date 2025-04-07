from turtle import Screen
import turtle as t
import random

mam = t.Turtle()
t.colormode(255)
mam.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

directions = [0, 90, 180, 270]
mam.pensize(15)
for i in range(200):
    for j in range(i):
        mam.color(random_color())
        mam.forward(30)
        mam.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()