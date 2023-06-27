import random as r
import hangman_resources as hr




min_reveal_count = 2; #this is always a constant

def occupy_list(list_x, n):
    for i in range(n):
        list_x.append("_");
    return list_x;

def choose_difficulty():
    levels = {1:['Easy', 4], 
              2: ['Medium', 2],
              3: ['Hard', 1]};
    
    difficulty = int(input("\nPlease choose a difficulty:\n1.Easy\n2.Medium\n3.Hard\n🖋️: "));
    if(1 <= difficulty <= 3):
        min_reveal_count = levels[difficulty][1]; #1 in this case being the position of the value to be used.       
    else:
        choose_difficulty();
    return min_reveal_count; 



def playHangman(word_list, stages):
    print(hr.logo)
    display = []
    chosen_word = r.choice(word_list)
    display = occupy_list(display, len(chosen_word))

    min_reveal_count = choose_difficulty();
    max_reveal_count = max(2, len(chosen_word) - 3); #this would range from 2 to the length of the word - 3, atleast to have the user guess 3 times.
    reveal_count = r.randint(min_reveal_count, max_reveal_count) #randomly selects the reveal count

    indices = r.sample(range(len(chosen_word)), reveal_count) #returns a list of possible indexes to reveal but with the size of reveal_count, using a range of len(chosen_word).

    for index in indices: # loops through the indices chosen from above to display them.
        display[index] = chosen_word[index]

    end_of_game = False
    lives = 6
    print(display)

    while not end_of_game:
        
        guess = input("Guess the right letter 🤔 >> ").lower()
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

        if guess not in chosen_word:
            lives -= 1            
            print(f"You have {lives} more lives.\n")
            if lives == 0:
                print(stages[lives])
                print(f"You Lost.\nThe word was {chosen_word}")
                break;

        if "_" not in display:
            print("You win!!!")
            print(f"{' '.join(display)} is the word\n")
            break

        print(display)
        print(stages[lives])
playHangman(hr.word_list, hr.stages);