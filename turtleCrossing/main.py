import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#! Initialising screen
screen = Screen(); #created the screen instance;
screen.setup(width=600, height=600); # setting dimensions of the screen.
screen.tracer(0); #ignores the animation and increases refresh rate.
screen.title("Turtle Cross");


# * Instantiated the player.
my_player = Player(); 

# * Instantiating and generating cars the car class.
#create a list of cars:
# for _ in range(20):
#     car = CarManager();
#     car.generate_random_car_position();
#     cars.append(car);

car = CarManager();



def is_6th_time(counter): 
    if counter > 0 and counter %6 == 0:
        return True;
    else:
        return False;


# $Key-Bindings:
screen.listen(); #this is necessary for your key bindings to work.
screen.onkey(fun=my_player.move_up,key="Up");


Game_Engine = True;
counter = 0;
fleet_of_cars = [car];

while Game_Engine:
    time.sleep(0.1);
    screen.update(); #works hand-in-hand with '.tracer()' to update the frames every 0.1 seconds.
    
    for car in fleet_of_cars:
        car.move();

    if is_6th_time(counter):
        new_car = car.generate_new_car();
        fleet_of_cars.append(new_car);

    counter+= 1;








# !end of screen
screen.exitonclick();