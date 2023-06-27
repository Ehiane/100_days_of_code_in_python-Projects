import random as r
import time as t

options = {
    1: {'name': 'Rock', 'image': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''},
    2: {'name': 'Paper', 'image': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''},
    3: {'name': 'Scissors', 'image': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}
}

clear_screen_command = '\033[H\033[J';

def playRockPaperScissors():
    print('''
          
.---.          .-.     .---.                       .--.      _                         
: .; :         : :.-.  : .; :                     : .--'    :_;                        
:   .'.--. .--.: `'.'  :  _..--. .---. .--..--.   `. `. .--..-..--. .--. .--..--. .--. 
: :.`' .; '  ..: . `.  : : ' .; ;: .; ' '_.: ..'   _`, '  ..: `._-.`._-.' .; : ..`._-.'
:_;:_`.__.`.__.:_;:_;  :_; `.__,_: ._.`.__.:_;    `.__.`.__.:_`.__.`.__.`.__.:_; `.__.'
                                 : :                                                   
                                 :_;                                                   
                                                                                                                                                                                                    
        ''')
    
    print("First player to reach a score of 5 wins the game.");

    user_score = 0;
    cpu_score = 0;
    round_count = 1;

    while user_score < 5 and cpu_score < 5:
        print(f"\nRound {round_count}")
        print(f"Scores:\nUser: {user_score}\tCPU: {cpu_score}\n")
        user_option = int(input("Choose:\n1: Rock\t2: Paper  3: Scissors\n>> "))
        cpu_option = r.randint(1, 3)
        user_choice = options[user_option]
        cpu_choice = options[cpu_option]

        print("User:")
        print(user_choice['image'])
        t.sleep(1)  # Add a delay of 1 second

        print("CPU:")
        print(cpu_choice['image'])
        t.sleep(1)  # Add a delay of 1 second

        if user_option == cpu_option:
            print("This was a draw!\n")
        elif (user_option == 1 and cpu_option == 3) or (user_option == 2 and cpu_option == 1) or (user_option == 3 and cpu_option == 2):
            print(f"User won!\n{user_choice['name']} beats {cpu_choice['name']} any day!\n")
            user_score += 1
        else:
            print(f"CPU won!\n{cpu_choice['name']} beats {user_choice['name']} any day!\n")
            cpu_score += 1

        round_count += 1
        print("-------------------------------------------------------------");

    print("Final Scores:")
    print(f"User: {user_score}\tCPU: {cpu_score}\n")

    if user_score > cpu_score:
        print("User wins the game!")
    else:
        print("CPU wins the game!")

    ans = input("Play again? (Y/N): ").lower()
    if ans == "y":
        print(clear_screen_command);
        playRockPaperScissors()

playRockPaperScissors()