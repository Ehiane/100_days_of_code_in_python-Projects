from turtle import Turtle;
import random as r;
RADIUS_STRETCH = 0.8;
VELCOCITY = [x for x in range(8,11+1)]; #let the velocity range from 8-11;

class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.pu(); 
        self.color("white");
        self.shape("circle"); #has default size of 20x20 pixel.
        self.x_velocity = r.choice(VELCOCITY);
        self.y_velocity = r.choice(VELCOCITY);
        self.trajectory = 0.1;
        # self.shapesize(RADIUS_STRETCH,RADIUS_STRETCH);
    
    def move(self):
        """
        the ball doesn't move at a current velocity. This was done on 
        purpose to add some realistic effect to the game.
        """

        new_x = self.xcor() + self.x_velocity;
        new_y = self.ycor() + self.y_velocity;
        self.goto(new_x,new_y);
        pass;

    def bounce_y(self):
        """
        y-coor will be mutable, x-coor will remain the same.
        """
        self.y_velocity *=-1;
        self.trajectory *= 0.95;
      
    def bounce_x(self):
        """
        x-coor will be mutable, y-coor will remain the same.
        """
        self.x_velocity *=-1;
        self.trajectory *= 0.95;
    
    def reset(self):
        self.clear();
        self.goto((0,0));
        self.trajectory = 0.1; #reset game_speed after a round loss
        self.bounce_x();

