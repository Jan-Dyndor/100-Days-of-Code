import turtle
import pandas as pd


def write_state_on_map(state_name, x_cor, y_cor):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x_cor, y_cor)
    state.write(state_name)

def not_guessed_states_to_csv(guessed_states, all_states):
    # not_guessed_states = []
    # for state in all_states:
    #     if state not in guessed_states:
    #         not_guessed_states.append(state)
    not_guessed_states = [state for state in all_states if state not in guessed_states]

    not_guessed_states_df = pd.DataFrame(not_guessed_states)
    not_guessed_states_df.to_csv("not_guessed_states.csv")



screen = turtle.Screen()
screen.title("U.S States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")

guessed = 0
should_continue = True
state_list = data["state"].to_list()
guessed_states = []

while should_continue:
    answer_state = screen.textinput(title=f"{guessed}/50 States Guessed", prompt="What's another state's name?").title()
    if guessed == 50:
        should_continue = False
    if answer_state == "Exit":
        not_guessed_states_to_csv(guessed_states=guessed_states, all_states=state_list)
        quit()
    if answer_state in state_list:
        guessed_states.append(answer_state)
        row = data[data["state"] == answer_state]
        X_cor = row["x"].values
        Y_cor = row["y"].values
        guessed += 1
        write_state_on_map(state_name=answer_state, x_cor=X_cor[0], y_cor=Y_cor[0])

turtle.mainloop()
