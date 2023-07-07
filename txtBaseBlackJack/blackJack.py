#######-----[ 🧢🪨: Black Jack]-----########

## TODO instead of hard coding list, use [LIST COMPREHENSION] --Done
## TODO use a dictionary to hold the values of the non numericals. --Done
## TODO create a print rules function and ask user if they want to view it at the start of the game.

#Import(s):
from resources import welcome_screen, start_pause, create_deck_of_cards, print_rules, stage1, stage2, User_score, User_deck, Computer_score,Computer_deck;





def initialize_game():
    welcome_screen()
    start_pause()

    game_deck = create_deck_of_cards()  # see <resources.py> for implementation.

    read_rules = input("Do you want to read the rules before playing? (yes/no): ").lower()

    if read_rules == "yes":
        print_rules()

    stage1(User_score, Computer_score, game_deck, User_deck, Computer_deck)

    draw_card_again = input("Do you want to draw another card? (yes/no): ").lower()

    stage2(User_score, User_deck, Computer_score, Computer_deck, game_deck)


initialize_game()