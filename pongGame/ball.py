from turtle import Turtle;
import random as r;
RADIUS_STRETCH = 0.8;


class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.pu(); 
        self.color("white");
        self.shape("circle"); #has default size of 20x20 pixel.
        # self.shapesize(RADIUS_STRETCH,RADIUS_STRETCH);
