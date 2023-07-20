from turtle import Turtle;

ALIGNMENT = "center";
FONT = ("Times", "15", "bold");


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.score = 0;
        self.highscore = 0;
        self.hideturtle();
        self.pu();
        self.font = FONT;
        self.color("white");
        self.goto((0,255));
        self.display_score();
        

    def display_score(self):
        """
        displays the score board once called at the center of the screen.
        """
        self.clear();
        self.write(arg=f"score: {self.score} High score: {self.highscore}",align=ALIGNMENT, font= self.font);

    def update_score(self):
        """
        increases the score by +1
        """
        self.score += 1;
        self.display_score();


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score;
        self.score = 0;
    

    def Write(self, text):
        """
        my personal default writing function, with preloaded font and alignment.
        """
        self.write(arg=text, align= ALIGNMENT, font=FONT);


    """
        def end_game(self):
        
            clears the screen and prints the 'game over' text
        
            self.clear();
            self.goto((0,0));
            self.write(arg= f"GAME OVER.\nYour score is {self.score}", align= ALIGNMENT, font= self.font);

    """