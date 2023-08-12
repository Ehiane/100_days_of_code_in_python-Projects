
# %Import(s):
from tkinter import *
import random as r;
import pandas;

# %Global(s):
#   *---UnMutable----# 
BACKGROUND_COLOR = "#B1DDC6"
FRONT = "images/card_front.png";
BACK = "images/card_back.png";
RIGHT = "images/right.png";
WRONG = "images/wrong.png";
TITLE_FONT = ("Ariel",60,"bold");
SUB_TITLE_FONT = ("Ariel", 40, "italic");
SOURCE = "data/igbo_words.csv";

starter_words = {
    "chi":"goddess",
    "efulefu": "zero",
    "egwugwu": "hardware",
    "ekwe": "allow"
}

#   *---Mutable----# 
foreign_language = "igbo";
base_languange = "english";
# ! this will change periodically
foreign_word, base_word = r.choice(list(starter_words.items()));



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
display_foreign_language = canvas.create_text(400,150, text=f"{foreign_language.capitalize()}", fill="black", font=SUB_TITLE_FONT);
display_foreign_word = canvas.create_text(400,263, text=f"{foreign_word}", fill="black", font=TITLE_FONT);

# display_base_language = canvas.create_text(400,150, text=f"{base_language.capitalize()}", fill="black", font=SUB_TITLE_FONT);
# display_base_word = canvas.create_text(400,263, text=f"{base_word}", fill="black", font=TITLE_FONT);



def pick_random_data(filename = SOURCE):
    global foreign_word, base_word;
    db = pandas.read_csv(filename);
    
    # local_db = db.to_dict(orient='records');
    # print(local_db);

    ## this works(i prefer this as it's (igbo word) to (english word), rather than igbo(igbo_word) -> english(english word))
    local_db = {row.Igbo: row.English for (index, row) in db.iterrows()}

    #pick a random pair from local_db; 
    chosen_pair = r.choice(list(local_db.items())); #returns a tuple.
    foreign_word, base_word = chosen_pair;

    canvas.itemconfigure(display_foreign_word, text=f"{foreign_word}");
    # canvas.itemconfigure(display_base_word, text=f"{base_word}");




    



##Button(s):
right_image = PhotoImage(file=RIGHT);
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50,command=pick_random_data);

left_image = PhotoImage(file=WRONG);
left_button = Button(image=left_image, highlightthickness=0, padx=50, pady=50, command=pick_random_data);


##Element Positioning:
canvas.grid(row=0, column=0, columnspan=2);
left_button.grid(row=1, column=0);
right_button.grid(row=1, column=1);




#* after a button is pressed then you can change the logo 



window.mainloop();