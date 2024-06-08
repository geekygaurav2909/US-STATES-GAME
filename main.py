from turtle import Turtle, Screen
import pandas as pd

game_on = True
live_left = False
incorrect_counter = 0
max_life = 3
screen = Screen()
screen.title("U.S STATE GAME")
screen.bgpic("blank_states_img.gif")

state_printer = Turtle()
state_printer.penup()

state_data = pd.read_csv("50_states.csv")
state_list = state_data.state.to_list()
guessed_state = []


while len(guessed_state) < 50 and game_on:
    # Get the input from the user
    score = len(guessed_state)
    if live_left:
        guess = screen.textinput(f"Wrong Guess: {score}/50 ", f"You have {max_life+1-incorrect_counter} live left. Try again:").title()
    else:
        guess = screen.textinput(f"State Guess: {score}/50 ", "Enter the state name:").title()

    if guess == "Exit":
        missed_states = [state for state in state_list if state not in guessed_state]
        state_to_learn = pd.DataFrame(missed_states)
        state_to_learn.to_csv("states_to_learn.csv", index=False, header=False)
        break

    # Compare the guess with existing states data
    # is_available = state_data[state_data.state == guess]

    if guess in state_list:
        live_left = False
        # Increase the score for every correct response
        score += 1
        guessed_state.append(guess)
        data = state_data[state_data.state == guess]

        x_value = data.x.iloc[0]
        y_value = data.y.iloc[0]

        # Taking the state data and printing it correctly on the map
        state_printer.goto(x_value, y_value)
        state_printer.ht()
        state_printer.write(f"{guess}", align= "center", font=("Arial",8,"normal"))
    else:
        incorrect_counter += 1
        if incorrect_counter <= 3:
            live_left = True        
        
        
    if incorrect_counter > max_life:
        state_printer.ht()
        state_printer.goto(0,280)
        state_printer.write(f"Your final score: {score}", align= "center", font=("Arial",14,"normal"))
        game_on = False
        


screen.exitonclick()