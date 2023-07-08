#####--------🔢🎰Number guesser-----####

from resources import logo, choose_level,cts, within_range , general_pause, replay, goodbye;

def guess():
    #ask player for difficulty & define the number to guess.
    print(logo);
    num_of_guesses, target, guessing_range = choose_level();
    play_again = False;
    
    while num_of_guesses > 0 and play_again == False:
        cts();
        print(logo);
        player_guess = int(input(f"You have {num_of_guesses} guess(es) remaining,\n\nyour specified level range is {guessing_range},\n\nwhat is your guess >>"))
        if(not within_range(player_guess,target, guessing_range) and player_guess < target):
            num_of_guesses -= 1; #decrement after every trial
            print("your guess is too low,");
            general_pause();
        elif(within_range(player_guess, target, guessing_range) and player_guess < target):
            num_of_guesses -=1;
            print("your guess is within the range of the target value!, try smth higher");
            general_pause();
        elif( not within_range(player_guess, target, guessing_range) and player_guess > target):
            num_of_guesses -= 1; #decrement after every trial
            print("your guess is too high,");
            general_pause();
        elif(within_range(player_guess, target, guessing_range) and player_guess > target):
            num_of_guesses -=1; #decrement after every trial
            print("your guess is within the range of the target value!, try smth lower");
            general_pause();
        elif(player_guess == target):
            print(f"you're right!\n you guessed the right number [{target}] !!");
            play_again = replay(play_again);
            if play_again == False:
                general_pause();
                print(goodbye);
                break;
    print(f"the target number is {target}"); 
    end_play_again = guess() if replay(play_again) else cts(), print(goodbye);
    end_play_again;

guess();




