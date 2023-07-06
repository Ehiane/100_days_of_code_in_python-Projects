# Hangman Game

## Demo
<img width="499" alt="Screenshot 2023-06-23 233530" src="https://github.com/Ehiane/advanced_rock_paper_scissors/assets/79903725/40d27150-1cc2-4d50-bfdc-b0893ab49aee">

This is a Python program that implements the classic game of Hangman. The objective of the game is to guess a secret word by guessing individual letters. The player has a limited number of attempts to guess the word correctly before losing the game.


## Requirements

To run this program, make sure you have the following:

- at least Python 3. {...} installed on your system.

## Getting Started

1. Clone the repository or download the Python script file.

2. Ensure that the `hangman_resources.py` file is in the same directory as the main script file.

3. Open a terminal or command prompt and navigate to the directory where the script file is located.

4. Run the following command to start the game:

   ```shell
   python hangman.py
   ```

## How to Play

1. Upon starting the game, the Hangman logo will be displayed.

2. You will be prompted to choose a difficulty level: Easy, Medium, or Hard. Enter the corresponding number (1, 2, or 3) to select the desired difficulty.

   - Easy: The word will have 4 letters, and a minimum of 2 letters will be revealed.
   - Medium: The word will have 2 letters, and a minimum of 2 letters will be revealed.
   - Hard: The word will have 1 letter, and a minimum of 2 letters will be revealed.

3. The game will randomly select a word from the word list based on the chosen difficulty.

4. A certain number of letters in the word will be revealed initially, as determined by the difficulty level. The remaining letters will be displayed as underscores.

5. The player can guess a letter by entering it at the prompt: "Guess the right letter 🤔 >>". Letters are not case-sensitive, so both uppercase and lowercase letters are accepted.

6. If the guessed letter is present in the word, it will be revealed in the corresponding positions. If the letter is not present, the player will lose a life. The number of remaining lives will be displayed.

7. The game continues until one of the following conditions is met:

   - The player correctly guesses all the letters in the word. In this case, the player wins the game.
   - The player runs out of lives. In this case, the player loses the game, and the secret word is revealed.

8. After the game ends, the player can choose to play again by running the script again.

## Customization

- The `hangman_resources.py` file contains the word list and ASCII art stages used for displaying the hangman. You can modify these resources to customize the game experience.

- To add or remove words from the word list, modify the `word_list` variable in the `hangman_resources.py` file.

- To customize the ASCII art stages, modify the `stages` list in the `hangman_resources.py` file. Each stage represents a different state of the hangman as the player loses lives.

## ASCII Art Stages

The game includes ASCII art stages to represent the hangman's progress as the player loses lives. The stages are defined in the `hangman_resources.py` file as follows:

```python
stages = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |


     /|   |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]
```

Feel free to modify or customize these stages to your liking. Each stage represents a visual depiction of the hangman's state at a certain point in the game.

## Acknowledgments

This Hangman game script was developed using Python and ASCII art resources from the `hangman_resources.py` file.

The `hangman_resources.py` file provides the necessary resources for the game, including the word list and ASCII art stages. The file is imported into the main script to access these resources.

## Author

This Hangman game was created by [Ehiane Oigiagbe(me)](https://github.com/ehiane) .
