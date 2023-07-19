import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#@ Globals:
ON, OFF = True, False;

#! Initialising screen
screen = Screen(); #created the screen instance;
screen.setup(width=600, height=600); # setting dimensions of the screen.
screen.tracer(0); #ignores the animation and increases refresh rate.
screen.title("Turtle Cross");


# * Instantiated the player.
my_player = Player(); 

# * Instantiating the car class.
first_car = CarManager();

#  *Instantiating the score board.
score_board = Scoreboard();

# $Key-Bindings:
screen.listen(); #this is necessary for your key bindings to work.
screen.onkey(fun=my_player.move_up,key="Up");


Game_Engine = True;
counter = 0;
fleet_of_cars = [first_car];

while Game_Engine:
    time.sleep(0.1);
    screen.update(); #works hand-in-hand with '.tracer()' to update the frames every 0.1 seconds.
    score_board.display_score();

    # Movement of cars
    for first_car in fleet_of_cars:
        first_car.move();

    # generating other cars
    if first_car.is_6th_time(counter):
        new_car = first_car.generate_new_car();
        fleet_of_cars.append(new_car);


    # Determining collision with turtle and cars 
    for car in fleet_of_cars:            
        if my_player.distance(car) < 25:
            # print endgame stuff and stop count;
            score_board.end_game();
            Game_Engine = OFF

    #Determine if the player is at the finish line:
    if my_player.is_at_finish_line():

        # change the level and reset the scoreboard;;
        my_player.reset();
        score_board.update_level();
        score_board.reset();

        # increase the speed of all the cars;
        for car in fleet_of_cars:
            car.speed_up();
        pass;

    

    counter+= 1; #used to help me generate other cars

# !end of screen
screen.exitonclick();