#Import(s):
from turtle import Turtle, Screen

#Object instantiation.
tim = Turtle();
screen = Screen();

#! start listening for events.
screen.listen();

#*Note: [this concept is called higher order function.]when using a function as a argument in another function, don't put the parenthesis.

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

screen.setup(width=500,height=400);
# how to prompt user
user_bet = screen.textinput(title="Make your bet", prompt="Which prompt will win the race? Enter a color: ");

print(user_bet); #printed to the screen.

# it's key to understand the coordinate system to know where to position objects  

"""
since the size of the width is 500 and tim is at the center(0,0), to move to the extreme end(by logic, it should be) (x=-250 and y =0), however, -250 is the exact edge of the window, so it wont actually display the object.
"""

offset = 15; 
x_coordinate = -(screen.window_width()/2 - offset)
tim.goto(x= x_coordinate, y=0);


# !end portion
screen.exitonclick();


