#------[Higher or Lower ]----#

##--------[Steps to take]------##
#@--------------------------[visuals]--------------------------------#
# 1. print both logos(i.e. "Higher Or Lower");
# 2. implement pause function
# 3. print first person , VS( as ascii art), the second person
# 4. after chosinng winner, implement pause, and go to next set, if passed.
# 
#@-------------------------[Code Implementation]---------------------# 
# 1. define play_game function
# 2. import database from gamedata file
# 3. import random module to chose two random celebrities from the database
# 4. use a while loop to traverse run the game.
# 5. compare the followers key, then determine the winner
# 6. once the player fails, the game ends the final score is printed out in the terminal.
# 7. print ending graphic

#$---IMPORT(s):
from game_data import data as database;
from game_functions import  cts, proceed,welcome_screen, show_celebrity_fact, error_handling, general_pause, stop_game;
import random as R;
from art import higher_or_lower;

# ! ---GLOBAL(s):
CELEB_1 = 1;
CELEB_2 = 2;
NAME  = 0;
DESCRIPTION = 1;
COUNTRY = 2;
FOLLOWERS = 3;


def play_game(database):
    #setting the game indicator to true as default, if the user gets one question wrong, it'll be false, game stops
    play_on = True; 
    score = 0;
  

    while(play_on):

        #PHASE 1 should return <option> and truth, needs database:

        #print welcome_screen
        welcome_screen(score);
        
        #display facts about celebrity
            #use random module to get a random index for the list;
        celeb_1_index, celeb_2_index = R.randrange(0, len(database)), R.randrange(0, len(database));
            #using the index, use array notation to find the details of the celeb.
        celeb_1_facts = [database[celeb_1_index]['name'],database[celeb_1_index]['description'], database[celeb_1_index]['country'], database[celeb_1_index]['follower_count_in_millions']];
        celeb_2_facts = [database[celeb_2_index]['name'],database[celeb_2_index]['description'], database[celeb_2_index]['country'], database[celeb_2_index]['follower_count_in_millions']];
        
        cts();
        if score > 0:
            print('\033[31m'+ f" \nCurrent Score: {score} " +'\033[0m' );
        print("Who do you think is:")
        print(higher_or_lower);
        

        if celeb_1_index != celeb_2_index: #to prevent comparing against the same person.
            option,truth = show_celebrity_fact(celeb_1_facts, celeb_2_facts);  #should return the right option.
        else:
            error_handling("the same person is being compared to! ")
            play_game(database);
        
        #PHASE 2: needs <option> and <truth>
        if option == CELEB_1 and truth != option:
            stop_game(score, celeb_2_facts[FOLLOWERS], celeb_2_facts[NAME], celeb_1_facts[FOLLOWERS], celeb_1_facts[NAME]);
            play_on = False;
            break;
        elif option == CELEB_2 and truth != option:
            stop_game(score, celeb_1_facts[FOLLOWERS], celeb_1_facts[NAME],celeb_2_facts[FOLLOWERS], celeb_2_facts[NAME] );
            play_on = False;
            break;
        elif option == CELEB_1 and truth == option:
            score = proceed(score);
        elif option == CELEB_2 and truth == option:
            score = proceed(score);


play_game(database);


