from turtle import Turtle, Screen

tutu = Turtle()
screen = Screen()

def move_forwards():
    tutu.forward(10)

def move_backwards():
    tutu.backward(10)

def counter_clockwise():
    tutu.left(10)

def clockwise():
    tutu.right(10)

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=tutu.reset)


screen.exitonclick()