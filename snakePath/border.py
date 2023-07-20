from turtle import Turtle;



class Boarder(Turtle):
    def __init__(self, window_length, window_width, color = "red"):
        super().__init__();
        self.pu();
        self.length = window_length;
        self.width = window_width;
        self.goto(-window_width/2, -window_length/2);
        self.pd();
        self.pensize(3);
        self.speed(0);
        self.color(color);

    def draw_border(self):
        for _ in range(2):
            self.forward(self.width);
            self.left(90);
            self.forward(self.length);
            self.left(90);
        
        self.hideturtle();

