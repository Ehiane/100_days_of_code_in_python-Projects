from turtle import Turtle;



# work on paddle movements
class Paddle(Turtle):
    def __init__(self, position,name,color = "red"):
        super().__init__();
        self.name = name;
        self.score = 0;
        self.pu();
        self.shape("square");
        self.shapesize(stretch_len=1.1, stretch_wid=3.5); #30x70
        self.goto(position);
        self.color(color);

    def get_player_name(self):
        pass;

    def up(self):
        new_y = self.ycor() + 20;
        self.goto(self.xcor(), new_y);

    def down(self):
        new_y = self.ycor() - 20;
        self.goto(self.xcor(), new_y);


