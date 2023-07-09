
#$---IMPORT(s):
from art import higher_or_lower, versus, oops, bust, correct;
from game_data import data as database;
import time


#! GLOBAL(s):
    #! Info for accessing celeb_fact_list in line[..]
        #!  0th :name, 1st item: description, 2nd item: country, 3rd item: followers

NAME  = 0;
DESCRIPTION = 1;
COUNTRY = 2;
FOLLOWERS = 3;

def print_red(message,expression =""):
    print('\033[31m' + message + '\033[0m');


def cts():
    """
    Clears the screen.
    
    Returns:
        None
    """
    print('\033[H\033[J')

def general_pause():
    """
    Pauses the terminal and waits for the user to press any key before advancing with the program.
    
    Returns:
        None
    """
    pause_time = True
    
    if pause_time:
        print("Press any Key to continue...")
        input()
    cts()  # clear the terminal.

def welcome_screen(score):
    print(higher_or_lower);
    print_red("Note!\nThese stats are as of dec 2021\n")
    if score > 0:
            print(f"\nCurrent Score: {score}");
    general_pause();

def print_vs():
    print(versus);


def loading_animation(text, duration=6):
    """
    Displays a loading animation effect.
    
    Args:
        text (str): The text to display along with the loading animation.
        duration (float, optional): The duration of the animation. Defaults to 6.

    Returns:
        None
    """
    start_time = time.time()  # get the start time
    end_time = start_time + duration  # calculate the end time
    while time.time() < end_time:
        for i in range(5):
            time.sleep(0.5)  # pause for half a second
            loading_message = f"{'.' * i}"
            print(f"{loading_message}\r{text}", end="", flush=True)  # print loading message with text below
        print("\r" + " " * 100 + "\r", end="")  # clear the line and overwrite it with 100 whitespaces
    print(f"Done {text}!")  # print a message when the animation is finished

def who_is_higher(celeb_1_followers, celeb_2_followers):
    output = 1 if celeb_1_followers > celeb_2_followers else 2; #they cant be equal, which is a prerequisite.
    return output;

def stop_game(score, winner_followers, winnwer_name, choice_followers, choice_name):
    cts();
    print(bust);

    print();
    loading_animation("calculating score ",2.5);
    print(f"😥\nBetter luck next time!\n*****************\nYour choice:\n**🪪: {choice_name}\n**👥: {choice_followers} million \n*****************\nThe correct answer:\n**🪪: {winnwer_name}\n**👥: {winner_followers} million\n*****************\nYour score is: {score}");



def show_celebrity_fact(celeb_fact_1, celeb_fact_2):
    if isinstance(celeb_fact_1, list) and isinstance(celeb_fact_2,list): #ensuring the data passed into the function is a list.
        if len(celeb_fact_1) == 4 and len(celeb_fact_2) == 4: #ensuring that there are three facts being passed into this function
            print(f"\n1: -------: [{celeb_fact_1[NAME]}] :-------\n**🖺: {celeb_fact_1[DESCRIPTION]}\n**🌍: {celeb_fact_1[COUNTRY]}.");
            print(f"\n2:-------: [{celeb_fact_2[NAME]}] :-------\n**🖺: {celeb_fact_2[DESCRIPTION]}\n**🌍: {celeb_fact_2[COUNTRY]}.");
        else:
            print("smth is missing in your list, not enough facts to process data.")
            return 0;
    else:
        print("Incorrect parameters");
        return 0;
    option = int(input("\nin terms of followers(in millions)\n❓: "));
    winner = who_is_higher(celeb_fact_1[FOLLOWERS], celeb_fact_2[FOLLOWERS]);
    return option,winner;



def error_handling(specific_message):
    cts();
    print(oops);
    loading_animation("trouble shooting", 2.5)
    print(f"\nSeems like smth went wrong,\nIt apppears that {specific_message}");
    loading_animation("restarting program", 2)
    general_pause();


def proceed(score):
    cts();
    print(correct);
    general_pause();
    return score + 1;