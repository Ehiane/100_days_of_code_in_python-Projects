
#imports
from database import *
import time;
from art import *

mutable_resources = {

    'water' : resources['water'],
    'coffee': resources['coffee'],
    'milk': resources['milk'],
}   


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


def printHelp():
    cts();
    print(help_art)
    print("Here are the following commands for this machine:\n\n['off'] - switches off the machine.\n['report'] - generates report of available resources\n['help'] - prints the help screen.\n['espresso'] - launches espresso maker\n['latte'] - launches latte maker\n['cappuccino'] - launches cappuccino maker");


def generate_report(price):
    print(report)
    company_profit = update_profit(price)
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}76g\nMoney: ${company_profit}");


def buy_drink(drink_type):
    drink_details = MENU[drink_type]; #type list

    if isinstance(drink_details, dict):
        if 'water' in drink_details['ingredients']:
            water = drink_details['ingredients']['water'];
        else:
            water = 0;
        
        if 'coffee' in drink_details['ingredients']:
            coffee = drink_details['ingredients']['coffee'];
        else:
            coffee = 0;
        
        if 'milk' in drink_details['ingredients']:
            milk = drink_details['ingredients']['milk'];
        else:
            milk = 0;
        
        
        #if we have all these resources.
        if is_resourceful(water, coffee, milk):
            drink_cost = drink_details['cost'];
            return drink_cost;
    else:
        return -1; #return a price, if resources aint available return -1;


def is_resourceful(num_water = 0, num_coffee = 0, num_milk = 0):
    updated_resource = update_resources(mutable_resources, num_water, num_coffee, num_milk);
    if len(updated_resource) > 0:
        print(f"resources remaining:\n{updated_resource}");
        return True;
    else:
        return False;


def update_resources(resource, water_used, coffee_used, milk_used):
    resource['water'] = mutable_resources['water'] - water_used;
    resource['coffee'] = mutable_resources['coffee'] - coffee_used;
    resource['milk'] = mutable_resources['milk'] - milk_used;

    if resource['water'] >= 0 and resource['coffee'] >= 0 and resource['milk'] >= 0:
        return resource;
    else:
        if resource['water'] < 0:
            print("sorry not enough water");
        if resource['coffee'] < 0:
            print("sorry not enough coffee");
        if resource['milk'] < 0:
            print("sorry not enough milk");
        return {};
        
def handle_null(currency):
    if currency == "":
        currency = "0";
        currency = float(currency);
    return currency;



def verify_payment(quarters, dimes, pennies, nickles):
    total = [];

    if quarters == "":
        quarters = handle_null(quarters);
        total.append(quarters);
    elif quarters != "":
        quarters = float(quarters) * 0.25;
        total.append(quarters);

    if dimes == "":
        dimes = handle_null(dimes);
        total.append(dimes);
    elif dimes != "":
        dimes = float(dimes) * 0.10;
        total.append(dimes);
    
    if pennies == "":
        pennies = handle_null(pennies);
        total.append(pennies);
    elif pennies != "":
        pennies = float(pennies) * 0.01;
        total.append(pennies);
    
    if nickles == "":
        nickles = handle_null(nickles);
        total.append(nickles);
    elif nickles != "":
        nickles = float(nickles) * 0.05;
        total.append(nickles);
    
    return total;




def process_payment(price):
    valid = False;
    save_company_profit(price);
    print(payment_section);


    print("\nInsert coins: ");
    print(f"the price is ${price}\n Method of payment: ");
    quaters = input("how many Quarters[0.25]: ");
    dimes = input("how many Dimes[0.10]: ");
    pennies = input("how many Pennies[0.01]: ");
    nickles = input("how many nickels[0.05]: ");

    loading_animation('verifying transaction ', 2);
    user_payment = verify_payment(quaters,dimes, pennies, nickles);
    user_payment = sum(user_payment);

    if user_payment == price:
        valid = True;
        print(f"Valid Transaction !\nThanks for your payment")
        if valid == True:
            company_profit = update_profit(user_payment);
            print(f"net profit = ${company_profit}")

    elif user_payment > price:
        valid = True;
        loading_animation('settling your change', 1.5);
        change = user_payment - price;
        
        company_profit = update_profit(user_payment);
        print(f"Valid Transaction\nThanks for your payment, here is your change: ${change} ")
    else:
        loading_animation('error detected', 2);
        print(f"Sorry that's not enough money, you spent {user_payment}, which is less than {price}.\nInvalid Transaction\nMoney Refunded.");
    
    return valid;


# prog_functions.py

def update_profit(price):
    # Read the contents of the file
    with open("coffeeMachineSoftware/data.txt", "r") as file:
        lines = file.readlines()

    # Modify the line containing the company_profit value
    for i in range(len(lines)):
        if lines[i].startswith("company_profit"):
            lines[i] = f"company_profit = {price}\n"
            break

    # Write the modified contents back to the file
    with open('coffeeMachineSoftware/data.txt', "w") as file:
        file.writelines(lines)

    return price

# prog_functions.py


def read_company_profit():
    # Read the value from the file
    with open("coffeeMachineSoftware/data.txt", "r") as file:
        line = file.readline().strip()

    # Extract the value from the line
    value = line.split("=")[1].strip()

    # Convert the value to a float or int if needed
    try:
        value = float(value)
    except ValueError:
        value = int(value)

    return value

# prog_functions.py

def save_company_profit(value):
    # Convert the value to a string representation
    value_str = str(value)

    # Prepare the content to write to the file
    content = f"company_profit = {value_str}\n"

    # Write the content to the file
    with open("coffeeMachineSoftware/data.txt", "w") as file:
        file.write(content)
