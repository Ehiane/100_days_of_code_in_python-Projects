from tkinter import *

THEME_COLOR = "#375362"
ALT_COLOR = "#000080"
FONT = ("Lucida Sans",50,"bold");

class QuizInterface(Tk):
    def __init__(self) -> None:
        ## Window configuration
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        ## Texts
        self.current_score = 0
        self.display_score =  Label(text=f'Score: {self.current_score}')

        ## Canvas
        self.question_canvas = Canvas(width=300,height=250,bg="#FFFFFF", highlightthickness=0)

        ## Images
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/true.png")

        ## Buttons
        self.true_btn = Button(image=self.true_img, highlightthickness=0, padx=50, pady=50, command= ...)
        self.false_btn = Button(image=self.false_img, highlightthickness=0, padx=50, pady=50, command= ...)

        ## Positioning
        self.display_score.grid(row=0,column=1)
        self.question_canvas.grid(row=1,column=0,columnspan=2)
        self.true_btn.grid(row=2,column=0)
        self.false_btn.grid(row=2,column=1)

        ## mainloop
        self.window.mainloop()