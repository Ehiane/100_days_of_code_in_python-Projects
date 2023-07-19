FONT = ("Courier", 20, "normal")
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
        self.hideturtle();
        self.display_score();

    def display_score(self):
        """
        displays the score on the screen.
        """
        self.goto(x=-220, y=240);
        self.write(font=FONT, align="center", arg= f"Level:{self.level}")


    def update_level(self):
        """
        updates the player level.
        """
        self.level += 1;


    def reset(self):
        """
        resets the scoreboard and displays updated score
        """
        self.clear();
        self.display_score();

    def end_game(self):
        """
        prints the game over function
        """
        self.clear();
        self.goto(0,0);
        self.write(font=FONT, align="center", arg= f"GAME OVER.")

