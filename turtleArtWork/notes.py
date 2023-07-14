# using tutle graphics to generate a random spot color art work
from turtle import Turtle, Screen, setup, screensize

import turtle as t
# importing the Turtle class;
import random as r

import math


# t.colormode(255);
# setup();
# screen = Screen();
# screen_size = screensize(2000,2000,'black');

# timmy = Turtle()
# timmy.shape("classic")
# timmy.color("BlueViolet")

def dashed_line(turtleObj, position):
    turtleObj.pendown()
    # toggles draw state off
    turtleObj.setx(position)
    turtleObj.penup()
    # toggles draw state off
    turtleObj.forward(10)


# start_position = 0;
# for i in range(20):
#     dashed_line(timmy,start_position);
#     start_position += 20;


def random_color():
    red = r.randint(0,255);
    green = r.randint(0,255);
    blue = r.randint(0,255);
    rgb = (red,green,blue);
    return rgb;


#--------------------------------------------[Exercise 1: connected Polygon shapes]------------------------------------------#

# def triangle(t, base, height=30):
#     t.color(random_color());
#     sides = 3
#     angle = get_angle(sides)

#     t.fd(base)
#     t.left(120 + angle)

#     for i in range(sides - 1):
#         t.forward(base + height)
#         t.right(angle)
#     t.forward(base + height)


# def square(turtleObj, length):
#     t.color(random_color());
#     sides = 4
#     angle = get_angle(sides)

#     for i in range(sides):
#         turtleObj.forward(length)
#         turtleObj.left(angle)


# def pentagon(t, length):
#     t.color(random_color());
#     sides = 5
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides):
#         t.left(angle)
#         t.fd(length)


# def hexagon(t, length):
#     t.color(random_color());
#     sides = 6
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides):
#         t.right(angle)
#         t.fd(length)


# def heptagon(t, length):
#     t.color(random_color());
#     sides = 7
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides - 2):
#         t.left(angle)
#         t.fd(length)
#     # it started messing up so i manually corrected it here
#     t.left(angle + 1.5)
#     t.fd(length + 8)
#     t.left(angle + 1.4)
#     t.fd(length)


# def octagon(t, length):
#     t.color(random_color());
#     sides = 8
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides):
#         t.right(angle)
#         t.fd(length)


# def nonagon(t, length):
#     t.color(random_color());
#     sides = 9
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides):
#         t.left(angle)
#         t.fd(length)


# def decagon(t, length):
#     t.color(random_color());
#     sides = 10
#     angle = get_angle(sides)

#     t.fd(length)
#     for i in range(sides):
#         t.right(angle)
#         t.fd(length)


# def get_angle(number_of_sides):
#     return int(360 / number_of_sides)


# base = int(input("what should your base be? suggestion:[100-300]"))
# height = int(input("what should your height be? suggestion: [30-80]"))

# to recenter the turtle
# timmy.penup();
# timmy.goto((100,220))
# timmy.pendown();

# triangle(timmy, 150, 30)
# # # triangle
# timmy.left(180)
# square(timmy, 150 + 30)
# # # square;
# pentagon(timmy, 150 + 30)
# # # pentagon
# timmy.left(180)
# hexagon(timmy, 150 + 30)
# timmy.right(180)
# heptagon(timmy, 150 + 30);
# timmy.left(180)
# octagon(timmy, 150 + 30)
# timmy.right(180)
# nonagon(timmy, 150 + 30)
# timmy.left(180)
# decagon(timmy, 150 + 30)



#my version is a bit more accurate, plus i dont know whats responsible for the glitch at heptagon.

# def draw_shape(t,num_side):
#     angle = get_angle(num_side);
#     for _ in range(num_side):
#         t.fd(100);
#         t.right(angle)

# for side in range(3,11):
#     timmy.color(r.choice(colors));
#     draw_shape(timmy,side);




#---------------------------------------[Exercise 2: random walk]----------------------------------------------#



# def get_thick(obj):
#     #change thickness size of the pen.
#     obj.begin_fill()
#     if obj.filling():
#         obj.pensize(12);



# def position_cursor(obj):
#     #handling positioning.
#     motion = {
#         1: obj.left,
#         2: obj.right,
#     }
#     option = r.randrange(1,3);
#     turn = motion[option];
#     turn(90);


# def constant_motion(obj):
#     #standard length of each stroke.
#     obj.fd(35);

# def pick_random_color(obj,colors):
#     #choosing a random color every time
#     obj.color(r.choice(colors));




# def random_walk(obj):
#     get_thick(obj);
#     obj.speed(10);
#     for _ in range(1000):
#         obj.color(random_color());
#         position_cursor(obj);
#         constant_motion(obj);


# random_walk(timmy);


# ------------------------------------------[Spirograph]--------------------------------------------------------------#

# timmy.speed('fastest');



# def draw_spirograph(gap_size):
#     for _ in range(int(360/gap_size)):
#         timmy.color(random_color())
#         timmy.circle(100);
#         timmy.setheading(timmy.heading()+gap_size);
        

# def draw_spirograph(gap_size):
#     for _ in range(360):
#         timmy.color(random_color())
#         timmy.circle(100);
#         timmy.left(5);
#         timmy.fd(0.5);

# draw_spirograph(5);

#done handling positioning.

# keep at the very bottom.
# timmy.end_fill(); #ends the thickness effect.

# screen.exitonclick()


# win_width, win_height, bg_color = 2000, 2000, 'black'

# turtle.setup()
# turtle.screensize(win_width, win_height, bg_color)

# timmy.goto((30,50));
