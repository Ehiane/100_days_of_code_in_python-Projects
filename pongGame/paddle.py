from turtle import Turtle;



# work on paddle movements
class Paddle(Turtle):
    def __init__(self, position, color = "red"):
        super().__init__();
        self.pu();
        self.shape("square");
        self.shapesize(stretch_len=1.1, stretch_wid=3.5);
        self.goto(position);
        self.color(color);

    def move(self,position):
        pass;

    def up(self):
        new_y = self.ycor() + 20;
        self.goto(self.xcor(), new_y);

    def down(self):
        new_y = self.ycor() - 20;
        self.goto(self.xcor(), new_y);
        
