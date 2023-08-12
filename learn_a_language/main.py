
# %Import(s):
from tkinter import *
import random as r;
import pandas;

# %Global(s):
BACKGROUND_COLOR = "#B1DDC6"
FRONT = "images/card_front.png";
BACK = "images/card_back.png";
RIGHT = "images/right.png";
WRONG = "images/wrong.png";
TITLE_FONT = ("Ariel",60,"bold");
SUB_TITLE_FONT = ("Ariel", 40, "italic");
SOURCE = "data/igbo_words.csv"

# --------------------- UI SET-UP ------------------------#
##Window setup:
window = Tk();
window.title("Flash-Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);


##Canvas Setup:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0);
card = PhotoImage(file=BACK)

#* start with the card displaying this first 
canvas.create_image(400, 275, image=card)

##Label(s):
foreign_language = "french";
canvas.create_text(400,150, text=f"{foreign_language.capitalize()}", fill="black", font=SUB_TITLE_FONT);

# ! this will change periodically
foreign_word = "trouve";
canvas.create_text(400,263, text=f"{foreign_word}", fill="black", font=TITLE_FONT);

def pick_random_data(filename = SOURCE):
    db = pandas.read_csv(filename);
    
    # local_db = db.to_dict(orient='records');
    # print(local_db);

    ## this works(i prefer this as it's (igbo word) to (english word), rather than igbo(igbo_word) -> english(english word))
    local_db = {row.Igbo: row.English for (index, row) in db.iterrows()}

    #pick a random pair from local_db; 
    chosen_pair = r.choice(list(local_db.items())); #returns a tuple.
    temp_foreign_word, temp_english_word = chosen_pair;
    
    return temp_foreign_word, temp_english_word;
    
    pass;

pick_random_data();

##Button(s):
right_image = PhotoImage(file=RIGHT);
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50);

left_image = PhotoImage(file=WRONG);
left_button = Button(image=left_image, highlightthickness=0, padx=50, pady=50);



##Element Positioning:
canvas.grid(row=0, column=0, columnspan=2);
left_button.grid(row=1, column=0);
right_button.grid(row=1, column=1);




#* after a button is pressed then you can change the logo 



window.mainloop();