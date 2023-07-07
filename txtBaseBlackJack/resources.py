import time;
import random as R

#Global Variable(s):
GAME_POINT = 21; #the number to match, if a number exceeds this, it's a bust.
LOW_BOUND = 17; #while the number is lesser than this, redraw from general deck;
User_score, Computer_score = 0,0;#setting both scores to 0
User_deck, Computer_deck = [],[]; #initialising both deck of cards.



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



def print_rules():
    print("#########-----[ 🧢🪨: Black Jack Rules]-----#########")
    print("* If the sum of your cards surpasses 21, it's a bust and you lose.")
    print("* While the total sum of your cards is less than 17, you must draw another card.")
    print("* If the sum is 17 or greater, you can choose to stop drawing cards.")
    print("* The player with a hand value higher than the other player wins.")
    print("* If both players have the same hand value, it's a draw.")
    print("* If any player has a hand value of 21, they automatically win.")
    print("* All non-numerical cards represent 10, except for an ACE (A).")
    print("* In this version of the game, the cards are not being removed from the deck.")
    print("* There are no joker cards.")
    print("####################################################")

def serve_both_cards(user_deck, computer_deck, game_deck):
    """
    Adds a random card to both user and computer decks from the game deck.

    Args:
        user_deck (list): The user's deck of cards.
        computer_deck (list): The computer's deck of cards.
        game_deck (list): The game deck of cards.

    Returns:
        None
    """
    user_card = R.choice(game_deck)
    computer_card = R.choice(game_deck)

    user_deck.append(user_card)
    computer_deck.append(computer_card)

def serve_single_card(deck, game_deck):
    """
    Adds a random card to a single deck from the game deck.

    Args:
        deck (list): The deck to which the card will be added.
        game_deck (list): The game deck of cards.

    Returns:
        None
    """
    card = R.choice(game_deck)
    deck.append(card)

def sum_up_deck(deck):
    """
    Calculates the sum of values in the deck.

    Args:
        deck (list): The deck of cards.

    Returns:
        int: The sum of the values in the deck.
    """
    return sum(deck)


def deal(user_score, computer_score, game_deck):
    """
    Distributes one card at a time to the players and updates their scores.

    Args:
        user_score (int): The current score of the user.
        computer_score (int): The current score of the computer.
        game_deck (list): The deck of cards.

    Returns:
        int: The updated score of the user.
        int: The updated score of the computer.
    """
    serve_single_card(User_deck, game_deck)
    serve_single_card(Computer_deck, game_deck)

    User_score = sum_up_deck(User_deck)
    Computer_score = sum_up_deck(Computer_deck)

    return User_score, Computer_score

def print_both_decks(user_deck, computer_deck):
    """
    Prints both the user's and computer's decks along with the sum of each deck.
    
    Args:
        user_deck (list): The user's deck of cards.
        computer_deck (list): The computer's deck of cards.
    
    Returns:
        None
    """
    print("\n\tUser's Deck:")
    print(f"\t{user_deck} = {sum(user_deck)}")
    
    print("\n\tComputer's Deck:")
    print(f"\t{computer_deck} = {sum(computer_deck)}\n")


def user_view_display(user_deck, computer_deck):
    """
    Displays the user's deck and the computer's deck (with the first card revealed).

    Args:
        user_deck (list): The user's deck of cards.
        computer_deck (list): The computer's deck of cards.

    Returns:
        None
    """
    print()
    loading_animation("Printing user's deck ", 2)
    print("\n\tUser's Deck:")
    print("\t", user_deck)

    print()
    loading_animation("Printing computer's deck ", 2)
    print("\n\tComputer's Deck:")
    print("\t", computer_deck, "\n") 

def determine_winner(user_score, user_deck, computer_score, computer_deck):
    """
    Determines the winner based on the scores and displays the result.

    Args:
        user_score (int): The score of the user.
        user_deck (list): The user's deck of cards.
        computer_score (int): The score of the computer.
        computer_deck (list): The computer's deck of cards.

    Returns:
        None
    """
    user_view_display(user_deck, computer_deck)

    if user_score > 21:
        print(computer_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Computer wins! You went over 21 (bust).")

    elif computer_score > 21:
        print(user_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Congratulations! Computer went over 21 (bust). You win!")

    elif user_score == 21 and computer_score != 21:
        print(user_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Congratulations! You got 21. You win!")

    elif computer_score == 21 and user_score != 21:
        print(computer_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Computer got 21. Computer wins!")

    elif user_score <= 21 and (user_score > computer_score or computer_score > 21):
        print(user_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Congratulations! Your score is higher. You win!")

    elif computer_score <= 21 and (computer_score > user_score or user_score > 21):
        print(computer_winner_logo)
        print_both_decks(user_deck, computer_deck)
        print("Computer's score is higher. Computer wins!")

    elif user_score == computer_score:
        print(draw_logo)
        print_both_decks(user_deck, computer_deck)
        print("It's a draw!")

    else:
        print("Error: Invalid game state.")  # This should never happen in a valid game.



def stage1(user_score, computer_score, game_deck, user_deck, computer_deck):
    """
    Executes stage 1 of the game, where each player is initially dealt one card.

    Args:
        user_score (int): The current score of the user.
        computer_score (int): The current score of the computer.
        game_deck (list): The deck of cards.
        user_deck (list): The user's deck of cards.
        computer_deck (list): The computer's deck of cards.

    Returns:
        None
    """
    user_score, computer_score = deal(user_score, computer_score, game_deck)

    user_view_display(user_deck, computer_deck)



def stage2(user_score, user_deck, computer_score, computer_deck, game_deck):
    """
    Executes stage 2 of the game, where additional cards are drawn if needed.

    Args:
        user_score (int): The current score of the user.
        user_deck (list): The user's deck of cards.
        computer_score (int): The current score of the computer.
        computer_deck (list): The computer's deck of cards.
        game_deck (list): The deck of cards.

    Returns:
        None
    """
    while True:
        cts()
        welcome_screen()
        user_view_display(user_deck, computer_deck)
        loading_animation("Dishing out cards ", 3)

        if user_score >= 21 or computer_score >= 21:
            break

        if user_score > 16:
            draw_card_again = input("Do you want to draw another card? [yes or no]\n>> ").lower()
            if draw_card_again == "no":
                break

        serve_single_card(User_deck, game_deck)
        serve_single_card(Computer_deck, game_deck)
        user_score = sum_up_deck(User_deck)
        computer_score = sum_up_deck(Computer_deck)

    cts()
    welcome_screen()
    loading_animation("Determining winner ", 3.5)
    cts()
    determine_winner(user_score, user_deck, computer_score, computer_deck)


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