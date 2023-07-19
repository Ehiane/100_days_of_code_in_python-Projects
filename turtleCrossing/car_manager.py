COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10; #per level.

#imports:
import random as r;
from turtle import Turtle;

class CarManager(Turtle):
    """
    This class deals with the random generation of cars.
    They should all ne generated and launched through the right side of the screen.
    """
    def __init__(self):
        super().__init__();
        self.pu();
        self.shape("square");
        self.shapesize(stretch_len=2); #making the car object a rectangular shape.
        self.color(r.choice(COLORS)); #choosing a random color for each car generated.
        self.mph = STARTING_MOVE_DISTANCE;
        self.generate_random_car_position();

    def generate_random_car_position(self):
        """
        Randomly generates the position for the car from the right side of the screen at different times
        and at different y positions.
        """
        y = r.randint(-230,230);
        self.goto(290, y);

    def move(self):
        """
        responsible for the constant movement of the car.
        """
        new_x = self.xcor() - self.mph;
        self.goto(new_x, self.ycor());        
        pass;

    def generate_new_car(self):
        """
        generates a new car instance once called.
        """
        new_car = self.__class__(); #had to search this up from stackoverflow.
        return new_car;

    def is_6th_time(self,counter):
        """
        checks if the iteration is at it 6th call
        """
        return True if counter > 0 and counter %6 == 0 else False;

    def speed_up(self):
        """
        increases the speed of the cars by +10 pixels;
        """
        self.mph += MOVE_INCREMENT;

