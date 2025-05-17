import turtle
from turtle import Turtle
import  pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
state_names = states_data["state"].tolist()

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Etats Trouvé.", prompt="Quel autre nom d'Etat ?")
    converted_answer = answer_state.title()
    if converted_answer == "Exit":
        # missed_state = []
        # for state in state_names:
        #     if state not in guessed_state:
        #         missed_state.append(state)
        missed_state = [state for state in state_names if state not in guessed_state]
        df = pandas.DataFrame(missed_state)
        df.to_csv("state_to_learn.csv")
        break
    if converted_answer in state_names:
        guessed_state.append(converted_answer)
        state = states_data[states_data.state == converted_answer]
        my_turtle = Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_position_x = state["x"].item()
        state_position_y = state["y"].item()
        my_turtle.goto(x=state_position_x, y=state_position_y)
        my_turtle.write(converted_answer)





