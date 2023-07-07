import time;
#this represents the values for all non numerical cards. Element 0 is the card name, Element 1 is the value.
SPECIAL_CARDS = {
    "A": ["Ace",11],
    "K": ["King", 10],
    "Q": ["Queen", 10],
}
CARD_NAME = 0;
CARD_VALUE = 1;

logo = """

                    ▄▄▄▄    ██▓    ▄▄▄      ▄████▄   ██ ▄█▀    ▄▄▄██▀▀▀▄▄▄      ▄████▄   ██ ▄█▀
                    ▓█████▄ ▓██▒   ▒████▄   ▒██▀ ▀█   ██▄█▒       ▒██  ▒████▄   ▒██▀ ▀█   ██▄█▒ 
                    ▒██▒ ▄██▒██░   ▒██  ▀█▄ ▒▓█    ▄ ▓███▄░       ░██  ▒██  ▀█▄ ▒▓█    ▄ ▓███▄░ 
                    ▒██░█▀  ▒██░   ░██▄▄▄▄██▒▓▓▄ ▄██▒▓██ █▄    ▓██▄██▓ ░██▄▄▄▄██▒▓▓▄ ▄██▒▓██ █▄ 
                    ░▓█  ▀█▓░██████▒▓█   ▓██▒ ▓███▀ ░▒██▒ █▄    ▓███▒   ▓█   ▓██▒ ▓███▀ ░▒██▒ █▄
                    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒▓▒▒░   ▒▒   ▓▒█░ ░▒ ▒  ░▒ ▒▒ ▓▒
                    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░ ░  ▒   ░ ░▒ ▒░    ▒ ░▒░    ▒   ▒▒ ░ ░  ▒   ░ ░▒ ▒░
                    ░    ░   ░ ░    ░   ▒  ░        ░ ░░ ░     ░ ░ ░    ░   ▒  ░        ░ ░░ ░ 
                    ░          ░  ░     ░  ░ ░      ░  ░       ░   ░        ░  ░ ░      ░  ░   
                        ░                 ░                                   ░               
"""

salutations = """

 █     █░▓█████  ██▓    ▄████▄  ▒█████   ███▄ ▄███▓▓█████                            ▄▄▄█████▓ ▒█████  
▓█░ █ ░█░▓█   ▀ ▓██▒   ▒██▀ ▀█ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀                            ▓  ██▒ ▓▒▒██▒  ██▒
▒█░ █ ░█ ▒███   ▒██░   ▒▓█    ▄▒██░  ██▒▓██    ▓██░▒███                              ▒ ▓██░ ▒░▒██░  ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░   ▒▓▓▄ ▄██▒██   ██░▒██    ▒██ ▒▓█  ▄                            ░ ▓██▓ ░ ▒██   ██░
░░██▒██▓ ░▒████▒░██████▒ ▓███▀ ░ ████▓▒░▒██▒   ░██▒░▒████▒                             ▒██▒ ░ ░ ████▓▒░
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░                             ▒ ░░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░ ░  ▒    ░ ▒ ▒░ ░  ░      ░ ░ ░  ░                               ░      ░ ▒ ▒░ 
  ░   ░     ░     ░ ░  ░       ░ ░ ░ ▒  ░      ░      ░                                ░      ░ ░ ░ ▒  
    ░       ░  ░    ░  ░ ░         ░ ░         ░      ░  ░                                        ░ ░  
                       ░                                                                               
"""


def cts():
    """
    [Void] to clear the screen;
    """
    print('\033[H\033[J');


def general_pause():
    """
    [Void] this function is similar to VScommunities implementation
    of system("pause"). It pauses the terminal and waits for the user
    to press any key before advancing with the program. 
    """
    pause_time = True;
    
    if pause_time:
        print("Press any Key to continue...");
        input();
    cts(); #clear the terminal.



def start_pause():
    """
    [Void] very similar to {general_pause()} but for starting the game only
    """
    pause_time = True;
    
    if pause_time:
        print("Press any Key to start...");
        input();
   


def welcome_screen():
    """
    [Void] prints the welcome screen for this program
    """
    print(salutations,"\n",logo);




def create_deck_of_cards():
    """
    [Array] This function returns the deck of cards used for this game.
    """
    #using list comprehension notation to generate the cards list
    cards = [x for x in range(2,11)]; 

    #inserting the special cards ACE, KING and Queen into the cards array
    #the indices are an intentional point of mine. 
    cards.insert(0,SPECIAL_CARDS["A"][CARD_VALUE]); 
    cards.insert(-1,SPECIAL_CARDS["K"][CARD_VALUE]);
    cards.insert(-1,SPECIAL_CARDS["Q"][CARD_VALUE]);
    return cards;


def loading_animation(text, duration=6):
    """
    [Void] from-->(Basic Banking app), displays a loading animation effect.
    """
    start_time = time.time() # get the start time
    end_time = start_time + duration # calculate the end time
    while time.time() < end_time:
        for i in range(5):
            time.sleep(0.5) # pause for half a second
            loading_message = f"{'.' * i}"
            print(f"{loading_message}\r{text}", end="", flush=True) # print loading message with text below
        print("\r" + " " * 100 + "\r", end="")  # clear the line and overwrite it with 100 whitespaces
    print(f"Done {text}!") # print a message when the animation is finished


user_winner_logo = """
 __      __  __                                           __    __                                                                    __     
/\ \    /\ \/\ \                           __            /\ \__/\ \                              __                                  /\ \    
\ \ \   \ \ \ \ \    ____    __  _ __     /\_\    ____   \ \ ,_\ \ \___      __       __  __  __/\_\    ___     ___      __  _ __    \ \ \   
 \ \ \   \ \ \ \ \  /',__\ /'__`/\`'__\   \/\ \  /',__\   \ \ \/\ \  _ `\  /'__`\    /\ \/\ \/\ \/\ \ /' _ `\ /' _ `\  /'__`/\`'__\   \ \ \  
  \ \_\   \ \ \_\ \/\__, `/\  __\ \ \/     \ \ \/\__, `\   \ \ \_\ \ \ \ \/\  __/    \ \ \_/ \_/ \ \ \/\ \/\ \/\ \/\ \/\  __\ \ \/     \ \_\ 
   \/\_\   \ \_____\/\____\ \____\ \_\      \ \_\/\____/    \ \__\\ \_\ \_\ \____\    \ \___x___/'\ \_\ \_\ \_\ \_\ \_\ \____\ \_\      \/\_\
    \/_/    \/_____/\/___/ \/____/\/_/       \/_/\/___/      \/__/ \/_/\/_/\/____/     \/__//__/   \/_/\/_/\/_/\/_/\/_/\/____/\/_/       \/_/

                                                                                                        
"""

computer_winner_logo = """
 __      ____                                      __                                     __    __                                                                    __     
/\ \    /\  _`\                                   /\ \__                   __            /\ \__/\ \                              __                                  /\ \    
\ \ \   \ \ \/\_\   ___    ___ ___   _____   __  _\ \ ,_\    __  _ __     /\_\    ____   \ \ ,_\ \ \___      __       __  __  __/\_\    ___     ___      __  _ __    \ \ \   
 \ \ \   \ \ \/_/_ / __`\/' __` __`\/\ '__`\/\ \/\ \ \ \/  /'__`/\`'__\   \/\ \  /',__\   \ \ \/\ \  _ `\  /'__`\    /\ \/\ \/\ \/\ \ /' _ `\ /' _ `\  /'__`/\`'__\   \ \ \  
  \ \_\   \ \ \L\ /\ \L\ /\ \/\ \/\ \ \ \L\ \ \ \_\ \ \ \_/\  __\ \ \/     \ \ \/\__, `\   \ \ \_\ \ \ \ \/\  __/    \ \ \_/ \_/ \ \ \/\ \/\ \/\ \/\ \/\  __\ \ \/     \ \_\ 
   \/\_\   \ \____\ \____\ \_\ \_\ \_\ \ ,__/\ \____/\ \__\ \____\ \_\      \ \_\/\____/    \ \__\\ \_\ \_\ \____\    \ \___x___/'\ \_\ \_\ \_\ \_\ \_\ \____\ \_\      \/\_\
    \/_/    \/___/ \/___/ \/_/\/_/\/_/\ \ \/  \/___/  \/__/\/____/\/_/       \/_/\/___/      \/__/ \/_/\/_/\/____/     \/__//__/   \/_/\/_/\/_/\/_/\/_/\/____/\/_/       \/_/
                                       \ \_\                                                                                                                                 
                                        \/_/                                                                                                                                 
"""

draw_logo = """
 __      ______  __                            ____                                 __     
/\ \    /\__  _\/\ \__                        /\  _`\                              /\ \    
\ \ \   \/_/\ \/\ \ ,_\   ____         __     \ \ \/\ \  _ __   __    __  __  __   \ \ \   
 \ \ \     \ \ \ \ \ \/  /',__\      /'__`\    \ \ \ \ \/\`'__/'__`\ /\ \/\ \/\ \   \ \ \  
  \ \_\     \_\ \_\ \ \_/\__, `\    /\ \L\.\_   \ \ \_\ \ \ \/\ \L\.\\ \ \_/ \_/ \   \ \_\ 
   \/\_\    /\_____\ \__\/\____/    \ \__/.\_\   \ \____/\ \_\ \__/.\_\ \___x___/'    \/\_\
    \/_/    \/_____/\/__/\/___/      \/__/\/_/    \/___/  \/_/\/__/\/_/\/__//__/       \/_/
                                                                                           
                                                                                           
"""