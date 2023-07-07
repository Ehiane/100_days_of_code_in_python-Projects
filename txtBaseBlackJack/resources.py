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


def start_pause():
    """
    Pauses the terminal and waits for the user to press any key before starting the game.
    
    Returns:
        None
    """
    pause_time = True
    
    if pause_time:
        print("Press any Key to start...")
        input()


def welcome_screen():
    """
    Prints the welcome screen for the program.
    
    Returns:
        None
    """
    print(salutations, "\n", logo)


def create_deck_of_cards():
    """
    Creates and returns the deck of cards used for the game.
    
    Returns:
        list: The deck of cards.
    """
    cards = [x for x in range(2, 11)]  # using list comprehension notation to generate the cards list

    # inserting the special cards ACE, KING, and Queen into the cards array
    cards.insert(0, SPECIAL_CARDS["A"][CARD_VALUE])
    cards.insert(-1, SPECIAL_CARDS["K"][CARD_VALUE])
    cards.insert(-1, SPECIAL_CARDS["Q"][CARD_VALUE])
    return cards


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



user_winner_logo = """

██╗   ██╗███████╗███████╗██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗    ██║    ██║██║████╗  ██║██╔════╝
██║   ██║███████╗█████╗  ██████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗
██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║███╗██║██║██║╚██╗██║╚════██║
╚██████╔╝███████║███████╗██║  ██║    ╚███╔███╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                                                                    
                                                                                                        
"""

computer_winner_logo = """

  ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗    ██║    ██║██║████╗  ██║██╔════╝
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗    ██║███╗██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║    ╚███╔███╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝

                                                                                                
"""

draw_logo = """
 ██████╗ ██████╗  █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║
██║  ██║██████╔╝███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══██║██║███╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ 
                                  
                                                                                           
"""