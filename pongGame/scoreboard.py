from turtle import Turtle;

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.color("white");
        self.penup();
        self.hideturtle();
        self.l_score = 0;
        self.r_score = 0;
        self.update_scoreboard();
      
    def update_scoreboard(self):
        """
        updates the scoreboard once its called by properly
        displaying texts on the screen in the right position.
        """
        self.goto(-100,200);
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200);
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_left_score(self):
        """
        updates the left score variable on the screen once called.
        """
        self.l_score += 1; 
        self.clear();
        self.update_scoreboard();

    def update_right_score(self):
        """
        updates the right score variable on the screen once called.
        """
        self.r_score += 1; 
        self.clear();
        self.update_scoreboard();
