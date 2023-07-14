# 🔢🎰Number guesser

## Demo
<img width="274" alt="Screenshot 2023-07-08 105812" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/edfb9759-5f7e-4dd7-a77f-fe3d454d5448">

<img width="254" alt="Screenshot 2023-07-08 105843" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/27b652ab-531f-4ab8-b660-39a7f1b02396">

<img width="408" alt="Screenshot 2023-07-08 105853" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/ea3408be-42ce-4b4f-a209-214ad6f885fb">


## Overview
The Number Guessing Game is a simple Python project where the player tries to guess a target number within a certain range. The game provides feedback on each guess and allows the player to play again.

## Getting Started
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```shell
    git clone https://github.com/Ehiane/100_days_of_code_in_python-Projects/numberGuesser.git
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
  

## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>
