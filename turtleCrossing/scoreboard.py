FONT = ("Courier", 24, "normal")
from turtle import Turtle;

class Scoreboard(Turtle):
    """
    Handles the level the player is currently on. 
    Also handles game over text.
    """
    def __init__(self):
        super().__init__();
        self.pu();
        self.color("black");
        self.level = 1;
        self.display_score();

    def display_score(self):
        self.goto(x=-280, y=280);
        self.write(font=FONT, align="center", arg= f"Level:{self.level}")


    def update_level(self):
        self.level += 1;


    def reset(self):
        self.clear();
        self.display_score();

    def end_game(self):
        self.clear();
        self.write(font=FONT, align="center", arg= f"GAME OVER.")

