import turtle
from turtle import Turtle,Screen
import pandas
screen=Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} 0/50 Guess the state"
                                    , prompt="what's another states name?").title()

    # If answer_state is one of the states in all states of the 50.csv
    # If they got right
    # Create a turtle to write the name of the state  at the state's x and y co-ordinate0

    #TODO Using normal Loop method

    # if answer_state=="Exit":
    #     missing_states=[]
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data=pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_learn.csv")

    #TODO Using List comprehension
    if answer_state == "Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


