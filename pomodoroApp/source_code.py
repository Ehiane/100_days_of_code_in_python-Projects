from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE = "pomodoroApp/tomato.png"
FONT = (FONT_NAME, 35, "bold");

#----------------------------- Functionality ----------------------------------#
# *1. choose task to do/perform
# *2. 25 mins of work for that task
# *3. 5 mins break.
#! 4. REPEAT STEPS 2-3, 3 TIMES
#* 5. Take a 20 min break.

#! REPEAT PROCESS TILL YOU'RE DONE WITH YOUR TASK.



# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
##   Window set-up;
window = Tk();
window.title("Pomodoro App");
window.config(padx=100, pady=50, bg=GREEN);

#*   Using Canvas widget.
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0);

#*   instantiating the image to the correct data type.
image_obj = PhotoImage(file=IMAGE);

#*   positioning the image on the canvas.(x=102,y=112)
canvas.create_image(100,112, image= image_obj);

#*   positioning the text on the canvas
canvas.create_text(103,130, text="00:00", fill="white", font= FONT);


#   using foreground(fg) element to edit color of text instead of background.

## Text(s)/Label(s):
timer_label = Label(text="Timer", font= FONT, foreground=PINK, bg= GREEN);
tick = Label(text="✔", foreground=PINK, background=GREEN);

## Button(s):
start_button = Button(text="Start", bg= PINK) #add command
reset_button = Button(text="Reset", bg= PINK) #add command




## Positioning:
timer_label.grid(column=1, row=0);
canvas.grid(column=1,row=1);
start_button.grid(column=0,row=2);
reset_button.grid(column=2,row=2);
tick.grid(column=1,row=3);





window.mainloop();