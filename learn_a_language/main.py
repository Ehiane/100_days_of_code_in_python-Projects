
# %Import(s):
from tkinter import *
import random as r;
import pandas;

# %Global(s):
#*----------------------Immutable-------------------------# 
BACKGROUND_COLOR = "#B1DDC6"
FRONT = "images/card_front.png";
BACK = "images/card_back.png";
RIGHT = "images/right.png";
WRONG = "images/wrong.png";
TITLE_FONT = ("Lucida Sans",50,"bold");
TIME_FONT = ("Lucida Sans",20,"bold");
SUB_TITLE_FONT = ("Lucida Sans", 40, "italic");
SOURCE = "data/igbo_words.csv";
GUESS_TIME = 5;
Timer = None;
STARTER_WORDS = {
    "chi":"goddess",
    "efulefu": "zero",
    "egwugwu": "hardware",
    "ekwe": "allow"
}
#*-----------------------Mutable---------------------------# 
foreign_language = "igbo";
base_languange = "english";
# ! this will change progamatically
foreign_word, base_word = r.choice(list(STARTER_WORDS.items()));
current_word_combo = (foreign_word,base_word);
foreign_word ="click a button to start";
#&--------------------Dictionaries-------------------------# 
local_db = {};
known_words = {};
unknown_words = {};

##---------------------------------------------------- FUNCTIONS -------------------------------------------------------#

def pick_random_data(filename = SOURCE):
    """
    Pick a random pair of words from the data file and return them.

    Args:
        filename (str): The path to the CSV data file.

    Returns:
        str, str: A tuple containing the randomly chosen foreign word and its translation.
    """
    global foreign_word, base_word, local_db;
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
    """
    Display a random word pair on the UI.
    """
    foreign, base = pick_random_data();
    

    canvas.itemconfigure(display_word, text=f"{foreign}");
    # canvas.itemconfigure(display_base_word, text=f"{base_word}");


def change_card_toFront():
    """
    Change the displayed card to the front side, showing the base language word.
    """
    global Timer;

    if Timer:
        window.after_cancel(Timer)  # Cancel existing timer, if any
    
    foreign, base = current_word_combo;

    # UI changes
    card.configure(file=FRONT)
    canvas.itemconfig(current_card, image=card)
    canvas.itemconfig(display_language, text=f"{base_languange}")
    canvas.itemconfig(display_word, text=f"{base}")


def change_card_toBack():
    """
    Change the displayed card to the back side, showing the foreign language word.
    """
    global Timer, current_word_combo;

    # cancel existing timer.
    if Timer:
        window.after_cancel(Timer) 

    # get new pair of data
    foreign, base = pick_random_data()
    current_word_combo = (foreign, base)

    # changing UI
    card.configure(file=BACK)
    canvas.itemconfig(current_card, image=card)
    canvas.itemconfig(display_language, text=f"{foreign_language}")
    canvas.itemconfig(display_word, text=f"{foreign}")

    # Start new timer immediately
    start_timer(GUESS_TIME)


def flip_card(filename = SOURCE):
    """
    Flip the card to show the opposite side after the timer expires.
    """
    global card,display_language,display_word,base_languange;
    change_card_toFront();


def start_timer(time_allowed):
    """
    Start the countdown timer with the given time allowance.

    Args:
        time_allowed (int): The time in seconds for the timer.
    """
    global Timer
    canvas.itemconfig(timer_text, text=f"0:{time_allowed:02}")
    Timer = window.after(1000, timer, time_allowed)


def timer(time_allowed):
    """
    Update the timer display and call flip_card when the timer reaches zero.

    Args:
        time_allowed (int): The remaining time on the timer.
    """
    global Timer
    sec = time_allowed % 60
    if time_allowed > 0:
        canvas.itemconfig(timer_text, text=f"0:{sec:02}")
        Timer = window.after(1000, timer, time_allowed - 1)
    else:
        canvas.itemconfig(timer_text, text="0:00")
        flip_card()


def user_knows():
    """
    Handle actions when the user knows the word, update data and UI.
    """
    global known_words, local_db
    foreign, base = current_word_combo

    to_insert = {foreign: base}
    known_words.update(to_insert)

    local_db.pop(foreign)
    # TODO: Save known words to a file
    save_to_file(filename="data/known_words.csv", dictionary=known_words)
    change_card_toBack()


def user_not_know():
    """
    Handle actions when the user does not know the word, update data and UI.
    """
    global unknown_words
    foreign, base = current_word_combo

    to_insert = {foreign: base}
    unknown_words.update(to_insert)

    # Don't remove word because you'd want it to repeat again.
    # Save unknown words to a file.
    save_to_file(filename="data/words_to_learn.csv", dictionary=unknown_words)
    change_card_toBack()


def save_to_file(filename,dictionary):
    """
    Save the given dictionary data to a CSV file.

    Args:
        filename (str): The path to the CSV file.
        dictionary (dict): The dictionary to be saved.
    """
    # reformating the dictionary to be acceptable for conversion to csv.
    raw_data = {'Igbo': list(dictionary.keys()),
                'English': list(dictionary.values())
                };
    # converting to dataframe.
    raw_dataFrame = pandas.DataFrame.from_dict(raw_data);
    # converting to csv
    raw_dataFrame.to_csv(filename,index=False);


##---------------------------------------------------- UI SET-UP -------------------------------------------------------#

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

##Button(s):
right_image = PhotoImage(file=RIGHT);
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50,command=user_knows);
left_image = PhotoImage(file=WRONG);
left_button = Button(image=left_image, highlightthickness=0, padx=50, pady=50, command=user_not_know);
start_button = Button(text="Start", command=change_card_toBack, bg="yellow",padx=30,pady=30,font=TIME_FONT);


##Element Positioning:
canvas.grid(row=1, column=0, columnspan=2);
left_button.grid(row=2, column=0);
right_button.grid(row=2, column=1);
start_button.place(x=335 ,y=525);





window.mainloop();