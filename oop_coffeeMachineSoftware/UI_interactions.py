
import time

def cts():
    """
    Clears the screen.
    
    Returns:
        None
    """
    print('\033[H\033[J')


def general_pause(message):
    """
    Pauses the terminal and waits for the user to press any key before advancing with the program.
    
    Returns:
        None
    """
    pause_time = True
    
    if pause_time:
        print(f"Press any Key to {message}...")
        input()
    cts()  # clear the terminal.


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


def printHelp(art):
    cts();
    print(art)
    print("Here are the following commands for this machine:\n\n['off'] - switches off the machine.\n['report'] - generates report of available resources\n['help'] - prints the help screen.\n['espresso'] - launches espresso maker\n['latte'] - launches latte maker\n['cappuccino'] - launches cappuccino maker");

