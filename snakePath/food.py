from turtle import Turtle;
import random as r;

class Food(Turtle):
    def __init__(self):
        super().__init__();
        self.shape("circle");
        self.pu();
        self.shapesize(stretch_len=0.5, stretch_wid=0.5); #the default size is 20x20 pixle, so using this function we are halving the size.
        self.color("red");
        self.speed("fastest"); #to avoid seeing it being created.
        self.refresh();

    def refresh(self):
        """
        updates the position of the food once called.
        """
        random_x = r.randint(-280,280);
        random_y = r.randint(-280,280);
        self.goto(x=random_x,y=random_y)
