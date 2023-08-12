
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
TIME_FONT = ("Ariel",20,"bold");
SUB_TITLE_FONT = ("Ariel", 40, "italic");
SOURCE = "data/igbo_words.csv";
GUESS_TIME = 5;

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
current_word_combo = (foreign_word,base_word);


# --------------------- UI SET-UP ------------------------#
##Window setup:
window = Tk();
window.title("Flash-Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);


##Canvas Setup:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0);
card = PhotoImage(file=BACK)

#* start with the card displaying this first 
current_card = canvas.create_image(400, 275, image=card)

##Label(s) and diplay:
display_language = canvas.create_text(400,150, text=f"{foreign_language.capitalize()}", fill="black", font=SUB_TITLE_FONT);
display_word = canvas.create_text(400,263, text=f"{foreign_word}", fill="black", font=TITLE_FONT);
timer_text = canvas.create_text(400, 100, text=f"0:0{GUESS_TIME}", fill="red", font=TIME_FONT);


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
    return foreign_word, base_word;


def display_random_pair():
    foreign, base = pick_random_data();
    

    canvas.itemconfigure(display_word, text=f"{foreign}");
    # canvas.itemconfigure(display_base_word, text=f"{base_word}");


def change_card_toFront():
    global current_word_combo;

    foreign, base = current_word_combo;
    # changing the card type:
    card.configure(file=FRONT);
    canvas.itemconfig(current_card,image=card)

    # changing the text:
    canvas.itemconfig(display_language, text=f"{base_languange}");
    canvas.itemconfig(display_word, text=f"{base}");
    timer();

def change_card_toBack():
    """
    this is the only function that calls the random data since it goes first.
    then the reverse card will have the translation of it.
    """
    global current_word_combo;
    
    foreign, base = pick_random_data();

    current_word_combo = (foreign,base);
    
    # changing the card type:
    card.configure(file=BACK);
    canvas.itemconfig(current_card,image=card)

    # changing the text:
    canvas.itemconfig(display_language, text=f"{foreign_language}");
    canvas.itemconfig(display_word, text=f"{foreign}");
    timer();



def flip_card(filename = SOURCE):
    """
    this will be called after the timer expires.
    """
    global card,display_language,display_word,base_languange;
    change_card_toFront();


def timer(time_allowed = GUESS_TIME):
    sec =  time_allowed % 60; #for future purposes.
    if sec >0:
        canvas.itemconfig(timer_text, text=f"0:0{sec}");
        time = window.after(1000,timer,sec-1);
    if sec == 0:
        canvas.itemconfig(timer_text, text=f"0:00");
        flip_card();





##Button(s):
right_image = PhotoImage(file=RIGHT);
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50,command=change_card_toBack);

left_image = PhotoImage(file=WRONG);
left_button = Button(image=left_image, highlightthickness=0, padx=50, pady=50, command=change_card_toBack);


##Element Positioning:
canvas.grid(row=1, column=0, columnspan=2);
left_button.grid(row=2, column=0);
right_button.grid(row=2, column=1);




#* after a button is pressed then you can change the logo 


window.mainloop();