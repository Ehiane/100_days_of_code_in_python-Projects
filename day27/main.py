import tkinter;

# initialising the window.
window = tkinter.Tk();
window.title("My first GUI progrm")

window.minsize(width=500, height=300);



# Label
myLabel = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"));
myLabel.pack(); #place's the lablel to the screen and centers it by default.
















# keeps the window on the screen.
window.mainloop();