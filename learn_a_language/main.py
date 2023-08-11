
# %Import(s):
from tkinter import *
import random as r;

# %Global(s):
BACKGROUND_COLOR = "#B1DDC6"
FRONT = "images/card_front.png";
BACK = "images/card_back.png";


# --------------------- UI SET-UP ------------------------#
##Window setup:
window = Tk();
window.title("Flash-Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);

##Canvas Setup:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0);

# *creating image_object;
card = PhotoImage(file=BACK)

#* start with the card displaying this first 
canvas.create_image(400, 275, image=card)

canvas.pack();

#* after a button is pressed then you can change the logo 



window.mainloop();