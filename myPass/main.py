# tried to import the passwordManager folder but didn't work.
from tkinter import *

# %Global(s):
LOGO = "myPass/logo.png"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk();
window.title("Password Manager")
window.config(padx=20, pady= 20)


canvas = Canvas(width=400, height= 400);

logo_obj = PhotoImage(file=LOGO);
canvas.create_image(200,200, image= logo_obj);

canvas.pack();


window.mainloop();