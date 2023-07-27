
#% IMPORT(s) 
from tkinter import *

#% GLOBAL(s)
FONT = ("Arial", 12);
RATE = 1.60934;

## window:
window = Tk();
window.title("Miles to Km Converter");
window.minsize(width=250, height= 100);

## input-box:
input_box = Entry(width=15);
input_box.grid(column=1, row=0);


def convert():
    global input_box;
    miles = float(input_box.get());
    km = miles * RATE;
    km = round(km,2);
    answer_label = Label(text=f"{km}", font= FONT);
    answer_label.grid(column=1, row=1);



##text(s)/label(s):
text_miles = Label(text="Miles", font= FONT);
text_converter = Label(text="is equal to", font= FONT);
text_unit = Label(text="Km");



## Button:
calculate_button = Button(text ="Calculate", command=convert); 

## Positioning:
text_miles.grid(column=2, row=0);
text_converter.grid(column=0, row=1);
text_unit.grid(column=2, row=1);
calculate_button.grid(column=1, row=2);

## Padding:
window.config(padx= 30, pady=30); 



window.mainloop();