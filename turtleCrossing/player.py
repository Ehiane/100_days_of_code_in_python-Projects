STARTING_POSITION = (0, -280);
MOVE_DISTANCE = 10;
FINISH_LINE_Y = 280;

#Imports:
from turtle import Turtle;

class Player(Turtle):
    """
    This class controls all the operations for the player.
    The player should be in the shape of a turtle and should move at the defined pace given above.
    """
    def __init__(self, player_color= "black"):
        super().__init__();
        self.pu(); #to stop drawing a line if moved.
        self.shape("turtle"); #setting the player's shape to a turtle;
        
        # giving the user the ability to change the turtle color if needed.
        self.player_color = player_color;
        self.color(self.player_color);
        
        #setting the player's starting position 
        self.goto(STARTING_POSITION);
        self.setheading(90);

    
    def move_up(self):
        """
        enables the player to move up by 10 pixels.
        """
        # change the y-coordinate;
        new_y = self.ycor() + MOVE_DISTANCE;
        self.goto(self.xcor(),new_y);

    def is_at_finish_line(self):
        """
        a boolean that returns true if at the finish line 
        and vice-versa.
        """
        return True if self.ycor() >= FINISH_LINE_Y else False;

    def reset(self):
        self.clear();
        self.goto(STARTING_POSITION);
