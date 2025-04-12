import turtle as t
from  turtle import Screen
import random

mam = t.Turtle()
t.colormode(255)
mam.shape("turtle")
mam.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range (100):
    mam.color(random_color())
    mam.circle(100)
    mam.setheading(mam.heading() + 10)



screen = Screen()
screen.exitonclick()