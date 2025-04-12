from turtle import Turtle, Screen
import turtle as t
import random


def get_color_fr(color):
    match color:
        case "red":
            return "rouge"
        case "orange":
            return "orange"
        case "yellow":
            return "jaune"
        case "green":
            return "verte"
        case "blue":
            return "bleu"
        case "indigo":
            return "indigo"
        case "purple":
            return "violete"

def get_color_en(color):
    match color:
        case "rouge":
            return "red"
        case "orange":
            return "orange"
        case "jaune":
            return "yellow"
        case "verte":
            return "yellow"
        case "bleu":
            return "blue"
        case "indigo":
            return "indigo"
        case "violette":
            return "purple"



screen = Screen()
screen.setup(width=900, height=600)
user_bet = get_color_en(screen.textinput(title="Faites un choix", prompt="Quelle tortue remportera la course ? Choisissez une couleur: "))
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
t.colormode(255)
is_race_on = False
all_turtles = []

new_y = -100
for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.goto(x=-430, y= new_y)
    new_y = new_y + 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 430:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Vous avez gagné ! La tortue {get_color_fr(winning_color)} est la tortue gagnante !")
            else:
                print(f"Vous avez perdu ! La tortue {get_color_fr(winning_color)} est la tortue gagnante !")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()