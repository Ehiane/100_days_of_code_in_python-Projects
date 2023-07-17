from turtle import Turtle;

ALIGNMENT = "center";
FONT = ("Times", "15", "bold");


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__();
        self.score = 0;
        self.hideturtle();
        self.pu();
        self.font = FONT;
        self.color("white");
        self.goto((0,255));
        self.display_score();
        

    def display_score(self):
        self.write(arg=f"score: {self.score}",align=ALIGNMENT, font= self.font);

    def update_score(self):
        self.clear();
        self.score += 1;
        self.display_score();

    def end_game(self):
        self.clear();
        self.goto((0,0));
        self.write(arg= f"GAME OVER.\nYour score is {self.score}", align= ALIGNMENT, font= self.font);

    def Write(self, text):
        self.write(arg=text, align= ALIGNMENT, font=FONT);