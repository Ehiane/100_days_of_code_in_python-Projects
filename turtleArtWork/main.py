# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('turtleArtWork/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r;
#     g = color.rgb.g;
#     b = color.rgb.b;
#     new_color = (r,g,b);
#     rgb_colors.append(new_color);

# print(rgb_colors)

import turtle as t
from notes import random_color;
import random as r

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


# 10 x 10 matrix, 20 in size per dot, 50 space in between
turtle = t.Turtle();
t.colormode(255);
t.setup();
screen = t.Screen();
screen_size = t.screensize(2000,2000,'black');


turtle.begin_fill();
if turtle.filling():
    turtle.pensize(20);
else:
    pass;


turtle.penup();
turtle.goto((-200,-100))
turtle.pendown();
turtle.hideturtle();

def paint_a_row(obj):
    for _ in range(10):
        obj.color(r.choice(color_list));
        obj.pendown();
        obj.fd(2);
        obj.penup();
        obj.fd(50);

    


def move_to_next_row_left(obj):
    obj.left(90);
    obj.penup();
    obj.fd(50);
    obj.left(90);
    obj.fd(50);
    #turn left or right

def move_to_next_row_right(obj):
    obj.right(90);
    obj.penup();
    obj.fd(50);
    obj.right(90);
    obj.fd(50);
    #turn left or right

def painting(obj):
    for _ in range(int(10/2)):
        paint_a_row(turtle);    
        move_to_next_row_left(turtle);
        paint_a_row(turtle);
        move_to_next_row_right(turtle);

painting(turtle);










screen.exitonclick()