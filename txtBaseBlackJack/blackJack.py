#######-----[ 🧢🪨: Black Jack]-----########
"""
*Rules:
*If the sum of your cards surpass 21, it's a bust and the player loses.
*while the total sum of your cards is lesser than 17, you must draw another card.
*if 17 or greater then you can submit your deck.
* who ever's card is lesser than 21 but higher than the other player wins.
* if both draw, no one wins the round
* if any of the player submits a 21, that player automatically wins
* all non-numerical cards represent 10, except an ACE(A);
* in this version of the game, the cards are not being removed from the deck
* They're no joker cards
"""

## TODO instead of hard coding list, use [LIST COMPREHENSION] --Done
## TODO use a dictionary to hold the values of the non numericals. --Done
## TODO create a print rules function and ask user if they want to view it at the start of the game.

#Import(s):
from resources import welcome_screen, cts, general_pause, start_pause, create_deck_of_cards, loading_animation, user_winner_logo, computer_winner_logo, draw_logo;
import random as R

#Global Variable(s):
GAME_POINT = 21; #the number to match, if a number exceeds this, it's a bust.
LOW_BOUND = 17; #while the number is lesser than this, redraw from general deck;
User_score, Computer_score = 0,0;#setting both scores to 0
User_deck, Computer_deck = [],[]; #initialising both deck of cards.

def serve_both_cards(user_deck, computer_deck,game_deck):
    """
    [Void*] this function adds a random card into both decks, one at a time. 
    """
    #getting the random indices for their card selection.
    user_random_choice = R.randint(0,len(game_deck) - 1);
    computer_random_choice = R.randint(0,len(game_deck) - 1);

    #adding the selections into their decks 
    user_deck.append(game_deck[user_random_choice]);
    computer_deck.append(game_deck[computer_random_choice]);
    ##Note: there's a little sense of vagueness if any of the decks get a 10, as a 10 could be a Q or K, 
            ##but for this project I wont focus too much on that, because the most important thing is the score.

def serve_single_card(deck,game_deck):
    """
    [Void*] this function adds a random card into a single deck. 
    """
    user_random_choice = R.randint(0,len(game_deck) - 1);    
    deck.append(game_deck[user_random_choice]);

def sum_up_deck(deck):
    total = 0;
    for value in deck:
        total += value;
    return total;

def deal(user_score, computer_score, game_deck):
    while(user_score < GAME_POINT or computer_score < GAME_POINT):
        #randomly distribute the cards to the players. --call serve card function.
        serve_both_cards(User_deck, Computer_deck, game_deck);
        User_score,Computer_score = sum_up_deck(User_deck), sum_up_deck(Computer_deck);
        user_score, computer_score = User_score, Computer_score;
        #if the sum of any of the decks are below 17, re serve the card
        if(User_score < LOW_BOUND):
            serve_single_card(User_deck,game_deck);
        if(Computer_score < LOW_BOUND):
            serve_single_card(Computer_deck, game_deck);
        return user_score, computer_score;

def print_both_decks(user_deck, computer_deck):
    print("\n\tUser's Deck: ");
    print("\t",user_deck);
    print("\n\tComputer's Deck: ");
    print("\t",computer_deck,"\n");

def user_view_display(user_deck, computer_deck):
    computer_last_card = computer_deck[-1];
    computer_deck.pop();
    computer_deck.append("{hidden}");

    print();
    loading_animation("printing user's deck ", 2);
    print("\n\tUser's Deck: ");
    print("\t",user_deck)

    print();
    loading_animation("printing computer's deck ", 2)
    print("\n\tComputer's Deck: ");
    print("\t",computer_deck,"\n");
    computer_deck.pop();
    computer_deck.append(computer_last_card); #adding it back 😂

def determine_winner(user_score, user_deck, computer_score, computer_deck):
    #reveal computer last  card --Done in user_view_display
    if user_score <= GAME_POINT and user_score > computer_score:
        print(user_winner_logo);
        print_both_decks(user_deck, computer_deck);
    
    elif computer_score <= GAME_POINT and computer_score > user_score:
        print(computer_winner_logo);  
        print_both_decks(user_deck, computer_deck);
    
    elif(computer_score == user_score):
        print(draw_logo);
        print_both_decks(user_deck, computer_deck);

def stage1(user_score,computer_score,game_deck,user_deck,computer_deck):
    user_score, computer_score = deal(user_score,computer_score,game_deck);
    #by this time both parties have 2 cards.
    user_view_display(user_deck, computer_deck);
    #prompt user if they want to keep their card or draw another one?

def stage2(user_score,user_deck,computer_score,computer_deck,game_deck, draw_card_again):
    if(draw_card_again == "yes"):
        cts();
        welcome_screen();
        user_score, computer_score = deal(user_score,computer_score, game_deck);
        
        loading_animation("Determining winner ", 3.5)
        cts();
        determine_winner(user_score,user_deck,computer_score,computer_deck);
    elif(draw_card_again == "no"):
        cts();
        welcome_screen();
        loading_animation("Determining winner ", 3.5)
        cts();
        determine_winner(user_score,user_deck,computer_score,computer_deck);
    else:
        print("Invalid option\nStart all over again\n");
        initialize_game();

def initialize_game():
    welcome_screen();
    start_pause();

    game_deck = create_deck_of_cards(); #see <resources.py> for implementation.
    
    stage1(User_score,Computer_score,game_deck,User_deck,Computer_deck);

    draw_card_again = input("Do you want to draw another card?[yes or no]\n>>").lower();

    stage2(User_score,User_deck,Computer_score,Computer_deck,game_deck,draw_card_again);


   

initialize_game();