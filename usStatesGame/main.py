
#% IMPORT(s). 
import turtle
import pandas

#@ CONSTANT(s).
 
FILE = "usStatesGame/50_states.csv"
FONT = ("Courier", 8, "normal")
IMAGE = "usStatesGame/blank_states_img.gif"
NUMBER_OF_STATES = 50
IMAGE_DIMENSION = (725, 491)
ON, OFF = True, False

#* Screen Details 
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=IMAGE_DIMENSION[0], height=IMAGE_DIMENSION[1])
screen.addshape(IMAGE)
turtle.shape(IMAGE)


#! GAME ESSENTIALS
Game_Engine = ON
correct_guesses = 0 
states_database = pandas.read_csv(FILE) #accessing the dataframe from the .csv file.
guessed_state = [] #used for accountability.


## HOW TO GET SPECIFIC X AND Y COORDINATES BY CLICKING ON THE SCREEN.
# def get_mouse_click_coor(x,y):
#     print(x,y);

# turtle.onscreenclick(get_mouse_click_coor);



# $ Activity: Read from the csv, get the x and y values, then ask the user for an answer
# check user's answer against all the state's and see if it matches them:
#  get the x and y values then display the text on that location
#  update the number of states gotten
# initialise the pandas dataframe

def reveal_state(x, y, state_data):
    """
    has a new turtle object that prints the result
    to the screen when called.
    """
    map_artist = turtle.Turtle()
    map_artist.hideturtle()
    map_artist.pu()
    map_artist.goto(x, y)
    state_name = refine_state_name(state_data)
    map_artist.write(arg=state_name, align="center", font=FONT)
    return state_name


def refine_state_name(series_obj_state_data):
    """
    refines the raw data given by pandas and just returns the state name.
    """
    if isinstance(series_obj_state_data, pandas.DataFrame):
        local_state_data = series_obj_state_data.state.item()
        state_name = local_state_data

    elif isinstance(series_obj_state_data, pandas.Series):
        local_state_data = series_obj_state_data.to_list()
        state_name = local_state_data[0]
    return state_name


def refine_coordinates(series_obj_x, series_obj_y):
    """
    accepts 2 series objects, converts the given data to a list using pandas,
    then breaks it down to the actual value you are looking for
    and returns it.
    """
    x_details = series_obj_x.to_list()
    y_details = series_obj_y.to_list()
    x = x_details[0]
    y = y_details[0]
    return x, y


def reveal_all_states(guessed_states=guessed_state, states_data_base=states_database):
    all_states = states_data_base["state"].to_list()
    print("Here are the states you failed to guess: \n")
    for state_data in all_states:
        if state_data not in guessed_states:
            # getting access of the row where state is present.
            state_raw_data = states_data_base[states_data_base["state"] == state_data]
            x, y = state_raw_data["x"].item(), state_raw_data["y"].item()
            failed_to_guess = reveal_state(x=x, y=y, state_data=state_raw_data)
            print(failed_to_guess)

    pass







def play(dataFrame):
    global correct_guesses, Game_Engine
    while Game_Engine and correct_guesses < NUMBER_OF_STATES:
        user_guess = screen.textinput(
            title=f"{correct_guesses} / {NUMBER_OF_STATES} States Correct",
            prompt="type 'quit' to quit at anytime ",
        ).title()

        if user_guess == "Quit":
            reveal_all_states()
            Game_Engine = OFF

        user_guess_row = dataFrame[dataFrame["state"] == user_guess]
        # getting the row of the guess if present.
        if len(user_guess_row) > 0:
            # answer should be valid.
            x_coordinate_info, y_coordinate_info = (
                user_guess_row["x"],
                user_guess_row["y"],
            )
            x, y = refine_coordinates(x_coordinate_info, y_coordinate_info)
            # i could have used .item();
            if user_guess_row.state.item() not in guessed_state:
                state_guessed = reveal_state(x=x, y=y, state_data=user_guess_row.state)
                guessed_state.append(state_guessed)
                correct_guesses += 1


play(states_database)
turtle.mainloop()
# does the same thing without exit on click
# screen.exitonclick();
