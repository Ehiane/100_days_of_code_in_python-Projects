from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
ALT_COLOR = "#000080"
FONT = ("Lucida Sans",20,"italic");
QUESTION_POSITION_ON_CANVAS = (150,125)

class QuizInterface(Tk):
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain

        ## Window configuration
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        ## Texts
        self.current_score = self.quiz.score
        self.display_score =  Label(text=f'Score: {self.current_score}', font=("Lucida Sans",10,"bold"), background=THEME_COLOR, fg="white")

        ## Canvas
        self.question_canvas = Canvas(width=300,height=250,bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            QUESTION_POSITION_ON_CANVAS,
            text="Some Question Text",
            width= 280,
            fill= THEME_COLOR,
            font=FONT)


        ## Images
        self.true_img = PhotoImage(file="ApiQuestionaire/images/true.png")
        self.false_img = PhotoImage(file="ApiQuestionaire/images/false.png")

        ## Buttons
        self.true_btn = Button(image=self.true_img, highlightthickness=0, padx=50, pady=50, command= self.trigger_true_btn)
        self.false_btn = Button(image=self.false_img, highlightthickness=0, padx=50, pady=50, command= self.trigger_false_btn)

        ## Positioning
        self.question_canvas.grid(row=1,column=0,columnspan=2, pady=50)
        self.display_score.grid(row=0,column=1)
        self.true_btn.grid(row=2,column=0)
        self.false_btn.grid(row=2,column=1)

        self.get_next_question()
        
        ## mainloop
        self.window.mainloop()
    
    def get_next_question(self):
        self.question_canvas.config(bg="white")
        self.display_score.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.question_canvas.itemconfig(self.question_text, text=q_text)
    
    def trigger_true_btn(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def trigger_false_btn(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    
    def give_feedback(self, is_valid):
        if is_valid: 
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



    
