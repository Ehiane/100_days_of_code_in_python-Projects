from tkinter import *

#$ initialising the window.

window = Tk();
window.title("My first GUI progrm");

window.minsize(width=500, height=300);



#$ Label

myLabel = Label(text="I am a label", font=("Arial", 24, "bold"));
myLabel.pack(); #place's the lablel to the screen and centers it by default.

myLabel["text"] = "New Text";
myLabel.config(text="NEW TEXT");

#$ BUTTON

button = Button(text="Click Me");
button.pack();













# keeps the window on the screen.
window.mainloop();