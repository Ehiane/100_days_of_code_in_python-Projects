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
        self.read_high_score();
        

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
        self.clear();
        self.display_score();
    

    def Write(self, text):
        """
        my personal default writing function, with preloaded font and alignment.
        """
        self.write(arg=text, align= ALIGNMENT, font=FONT);

    def save_high_score(self):
        with open("snakePath/score_data.txt","w") as file:
            file.write(f"High Score: {self.highscore}  \nCurrent Score: {self.score}  ");
    

    def read_high_score(self):
        with open("snakePath/score_data.txt","r") as file:
            lines = file.readlines();
            print(lines[0]);
            if len(lines) != 0:
                score = lines[0][12:-1]; #from that index to the last part of the line.
                self.highscore = int(score);
                  
    

    """
        def end_game(self):
        
            clears the screen and prints the 'game over' text
        
            self.clear();
            self.goto((0,0));
            self.write(arg= f"GAME OVER.\nYour score is {self.score}", align= ALIGNMENT, font= self.font);

    """