import dependecies as extrnl

cls = extrnl.clear_screen_command;

def stop_game(indicator):
    Q = input("Do you want to keep playing?\n[Yes or No]\n>>").lower()
    if Q == "no" and isinstance(indicator, bool):
        indicator = False
        return indicator
    elif (isinstance(indicator, bool) != True):
        print("Incorrect argument type!")
    else:
        return indicator;

def determine_winner(database):
    highest_bid = 0;
    highest_bidder = "";
    for key,value in database.items():
        highest_bid = value if value > highest_bid else highest_bid;
        highest_bidder = key if value == highest_bid else highest_bidder
    winner_details = [highest_bidder, highest_bid];
    return winner_details;

def start_game():
    database = {}
    proceed = True
    while (proceed):
        print(extrnl.start_logo,"\n",extrnl.title_logo);
        username = input("What is your name? ")
        userBid = int(input("What is your bid? $"))
        database[username] = userBid
        proceed = stop_game(proceed)
        print(cls);
    print(f"\t\tHere are the stats:\n{database}");
    winner_details = determine_winner(database);
    winner, highest_bid = winner_details;
    
    print(f"\n{extrnl.winner_logo}\nThe winner is {winner} with a bid of {highest_bid}");

start_game();
