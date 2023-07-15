from turtle import Turtle, Screen


tim = Turtle();
screen = Screen();







# start listening for events.
screen.listen();

##Note: [this concept is called higher order function.]when using a function as a argument in another function, don't put the parenthesis.

# screen.onkey(key="space", fun=move_forwards); #has to args: (funct, key)... what you want it to do when you press key


# Creating etch-a-sketch
# W - fd
# S - bck
# A - counter-clockwise(tilt left)
# D - clockwise(tilt right)
# C - clear and reposition.

# making the functions to carry out events.
def move_forwards():
    tim.forward(10);

def move_backwards():
    tim.backward(10);

def turn_counterClockwise():
    tim.left(30);

def turn_clockwise():
    tim.right(-30);

def clear():
    screen.clear();

screen.onkey(key="w",fun=move_forwards);
screen.onkey(key="s",fun=move_backwards);
screen.onkey(key="a",fun=turn_counterClockwise);
screen.onkey(key="d",fun=turn_clockwise);
screen.onkey(key="c",fun=clear);








screen.exitonclick();


