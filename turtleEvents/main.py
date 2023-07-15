#Import(s):
from turtle import Turtle, Screen
import random as r

#Object instantiation.
# tim = Turtle();
screen = Screen();

#! start listening for events.
screen.listen();

#*Note: [this concept is called higher order function.]when using a function as a argument in another function, don't put the parenthesis.

# tim.shape("turtle");
# screen.onkey(key="space", fun=move_forwards); #has to args: (funct, key)... what you want it to do when you press key


# ------------------------[Creating etch-a-sketch]-------------------------------------
# W - fd
# S - bck
# A - counter-clockwise(tilt left)
# D - clockwise(tilt right)
# C - clear and reposition.

# making the functions to carry out events.
# def move_forwards():
#     tim.forward(10);

# def move_backwards():
#     tim.backward(10);

# def turn_counterClockwise():
#     new_heading = tim.heading() + 10;
#     tim.setheading(new_heading);

# def turn_clockwise():
#     new_heading = tim.heading() - 10;
#     tim.setheading(new_heading);

# def clear():
#     tim.clear();
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.onkey(key="w",fun=move_forwards);
# screen.onkey(key="s",fun=move_backwards);
# screen.onkey(key="a",fun=turn_counterClockwise);
# screen.onkey(key="d",fun=turn_clockwise);
# screen.onkey(key="c",fun=clear);

#-------------------------[race]-------------------------------------------------------
is_race_on = False

screen.setup(width=500,height=400);
# how to prompt user
user_bet = screen.textinput(title="Make your bet", prompt="Which prompt will win the race? Enter a color: ");
# print(user_bet); #printed to the screen.

colors = ["red", "orange", "yellow","green", "blue", "purple"]

# it's key to understand the coordinate system to know where to position objects  

"""
since the size of the width is 500 and tim is at the center(0,0), to move to the extreme end(by logic, it should be) (x=-250 and y =0), however, -250 is the exact edge of the window, so it wont actually display the object.
"""

# creating 6 turtles.

y_positions = [0,-50,50,-100,100,150,-150];

turtle_speeds = [x for x in range(11)]; #using list comprehension.
turtle_racers = [];
# first turtle
offset = 15; 
x_coordinate = -(screen.window_width()/2 - offset);
# tim.pu(); #pu - penup
#changed the shape to a turtle.


def initialise_turtles(colors, y_positions):
    for lane in range(6):
        new_turtle =  Turtle(shape="turtle");
        new_turtle.color(colors[lane]);
        new_turtle.pu();
        new_turtle.goto(x= x_coordinate,y = y_positions[lane]);
        turtle_racers.append(new_turtle);

initialise_turtles(colors, y_positions);



if user_bet:
    is_race_on = True;

while is_race_on:
    finish_line_reached = False;
    for turtle_racer in turtle_racers:

        if turtle_racer.xcor() > abs(x_coordinate):
            winning_color = turtle_racer.pencolor();
            if winning_color == user_bet:
                print(f"YAY!!! you won the race!! {user_bet} is the winning color");
            else:
                print(f"YAY!!! you won the race!! {user_bet} is the winning color")
            is_race_on = False;
            break;


        random_speed = r.choice(turtle_speeds);
        turtle_racer.fd(random_speed)






# !end portion
screen.exitonclick();


