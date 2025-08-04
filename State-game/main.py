import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Setup writer
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Load data
df = pd.read_csv('50_states.csv')
state_list = df['state'].tolist()

# Game state
guessed_states = []
count = 0

while len(guessed_states) < 50:
    screen.title(f"{count}/50 U.S. States Correct")
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state is None:
        break  # User cancelled

    answer_state = answer_state.title()  # Normalize case (e.g., texas -> Texas)

    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        count += 1

        # Get coordinates and write state name
        state_row = df[df["state"] == answer_state]
        x_cor = int(state_row['x'].values[0])
        y_cor = int(state_row['y'].values[0])
        writer.goto(x_cor, y_cor)
        writer.write(answer_state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
