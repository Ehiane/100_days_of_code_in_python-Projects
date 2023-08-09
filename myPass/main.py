# tried to import the passwordManager folder: it worked.
# import sys
# import os

# # Add the path to the root directory (folder of folders) to sys.path
# root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(root_directory)

# # Now you can import the module
# from passwordGenerator.complexPasswordGenerator import random_password_generator

from tkinter import *

# %Global(s):
LOGO = "logo.png"
FONT = ("Courier",12);
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
##Window setup:
window = Tk();
window.title("Password Manager")
window.config(padx=50, pady= 50)

##Canvas Setup:
canvas = Canvas(width=200, height= 200);

#*creating image_object;
logo_obj = PhotoImage(file=LOGO);

canvas.create_image(100,100, image= logo_obj);

##Label(s):
website_label = Label(text="Website:",font= FONT);
userID_label = Label(text="Email/Username:", font=FONT);
password_label = Label(text="Password:",font= FONT);

##Entry(s):
website_input = Entry(width=35,justify="left");
userID_input = Entry(width=35,justify="left");
password_input= Entry(width=21,justify="left");

website_label.focus(); #! Sets the cursor to this entry at the start of the program.

##Button(s):
generate_password_button = Button(text="Generate Password"); #add command
add_button= Button(text="Add", width=36); #add command


##Element positioning:
canvas.grid(column=1, row=0);
website_label.grid(column=0, row=1);
website_input.grid(column=1, row=1, columnspan=2);
userID_label.grid(column=0, row=2);
userID_input.grid(column=1, row=2, columnspan=2);
password_input.grid(column=1, row=3);
password_label.grid(column=0,row=3);
generate_password_button.grid(column=2,row=3);
add_button.grid(column=1, row=4, columnspan=2);


window.mainloop();