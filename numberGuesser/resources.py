import random as R;

logo = """
 ██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                  
"""

goodbye = """
  _______ _                 _           __             _____  _             _             
 |__   __| |               | |         / _|           |  __ \| |           (_)            
    | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| |  ___/| |/ _` | | | | | '_ \ / _` |
    | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |    | | (_| | |_| | | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, |
                                                                       __/ |         __/ |
                                                                      |___/         |___/ 
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

def choose_level():
    """
    returns number of guesses based on level
    """
    level = input("What level would you like to play on?\n[Easy or Hard]\n>>").lower();
    levels = {
        "easy": [10, R.randint(0,50), 5],
        "hard": [5, R.randint(0,100), 2],
    }
    return levels[level];

def within_range(guess, target, guessing_range):
    """
    Check if the guess is within a certain range of the target number.

    Args:
        guess (int): The number guessed by the player.
        target (int): The target number to compare against.
        guessing_range (int): The range within which the guess is considered correct.

    Returns:
        bool: True if the guess is within the specified range, False otherwise.
    """

    lower_limit = target - guessing_range
    higher_limit = target + guessing_range
    return lower_limit <= guess <= higher_limit


def replay(return_indicator):
    """
    Ask the player if they want to play again and return the corresponding indicator.

    Args:
        return_indicator (bool): The current indicator value.

    Returns:
        bool: Updated indicator value based on the player's choice.

    """
    indicator = input("Would you like to play again?\n[yes or no]\n>>").lower()
    if indicator == "yes":
        return_indicator = True
        return return_indicator
    elif indicator == "no":
        return_indicator = False
        return return_indicator
    else:
        print("Invalid option")
        return replay(False)
