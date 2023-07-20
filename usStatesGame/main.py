import turtle;
import pandas;

FILE = "usStatesGame/50_states.csv";
FONT= ("Courier", 10, "normal");
IMAGE = "usStatesGame/blank_states_img.gif"
NUMBER_OF_STATES = 50;


screen = turtle.Screen();
screen.title("U.S. States Game");
screen.addshape(IMAGE);

ON, OFF = True, False;

turtle.shape(IMAGE);

# def get_mouse_click_coor(x,y):
#     print(x,y);

# turtle.onscreenclick(get_mouse_click_coor);

def reveal_state(x,y,state_data):
    turtle.pu();
    turtle.goto(x,y);
    state_name = refine_state_name(state_data);
    turtle.write(arg= state_name, align= "center", font= FONT);


def refine_state_name(series_obj_state_data):
    """
    refines the raw data given by pandas and just returns the state name.
    """
    state_data = series_obj_state_data.to_list();
    state_name = state_data[0];
    return state_name;


def refine_coordinates(series_obj_x, series_obj_y):
    """
    accepts 2 series objects, converts the given data to a list using pandas,
    then breaks it down to the actual value you are looking for
    and returns it.
    """
    x_details = series_obj_x.to_list();
    y_details = series_obj_y.to_list();
    x = x_details[0];
    y = y_details[0];
    return x,y;

#$ Activity: Read from the csv, get the x and y values, then ask the user for an answer
# check user's answer against all the state's and see if it matches them:
#  get the x and y values then display the text on that location
#  update the number of states gotten

# initialise the pandas dataframe
states_database = pandas.read_csv(FILE);

Game_Engine = ON;
correct_guesses = 0;

def play(dataFrame):
    while(Game_Engine and correct_guesses < NUMBER_OF_STATES):
        user_guess = screen.textinput(title="Guess a State", prompt="state name 🗺️").title();
        user_guess_row = dataFrame[dataFrame["state"] == user_guess ]; 
        if len(user_guess_row) > 0:
            # answer should be valid.
            x_coordinate_info,y_coordinate_info = user_guess_row["x"], user_guess_row["y"]; 
            x,y = refine_coordinates(x_coordinate_info,y_coordinate_info);
            reveal_state(x= x, y= y, state_data= user_guess_row.state);
            pass;






play(states_database);
turtle.mainloop(); #does the same thing without exit on click
# screen.exitonclick();