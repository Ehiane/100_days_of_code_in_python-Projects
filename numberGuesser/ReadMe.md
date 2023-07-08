# 🔢🎰Number guesser

## Overview
The Number Guessing Game is a simple Python project where the player tries to guess a target number within a certain range. The game provides feedback on each guess and allows the player to play again.

## Getting Started
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/number-guessing-game.git
   ```
2. Navigate to the project directory:
   ```shell
   cd number-guessing-game
   ```
3. Run the game:
   ```shell
   guessing_machine.py
   ```

## Game Rules
1. The game generates a random target number within a predefined range.
2. The player needs to guess the target number.
3. The player has multiple attempts to guess the number.
4. After each guess, the game provides feedback on whether the guess is too high or too low.
5. The game ends when the player guesses the correct number or runs out of attempts.


## Functions
### within_range(guess, target, guessing_range)
* Check if the guess is within a certain range of the target number.
  #### Arguments
  * guess (int): The number guessed by the player.
  * target (int): The target number to compare against.
  * guessing_range (int): The range within which the guess is considered correct.
  #### Returns
  * True if the guess is within the specified range.
  * False otherwise.

### replay(return_indicator)
  * Ask the player if they want to play again and return the corresponding indicator.
  
  #### Arguments
  * return_indicator (bool): The current indicator value.
  ##### Returns
  * Updated indicator value based on the player's choice (True or False).

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


## License
This project is licensed under the MIT License.
  
