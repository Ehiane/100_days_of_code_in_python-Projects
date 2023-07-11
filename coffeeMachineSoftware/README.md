# ☕🤖| Coffee Machine Software

This repository contains the source code for a coffee machine software. The software allows users to interact with the coffee machine, make various types of coffee, check resources, process payments, and generate reports.

## Demo
![bean-haven demo gif](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5c0a02e9-bc82-47d0-a652-67deb7f96fe7)

## Program Requirements

The coffee machine software fulfills the following requirements:

1. **Print Report**: Users can generate a report that displays the current status of the coffee machine, including the company's profit and available resources.

2. **Check Resources**: The software checks if there are sufficient resources (water, milk, and coffee) available in the machine before preparing a coffee.

3. **Process Coins**: The software handles the payment process by accepting coins from the user and calculating the total payment amount.

4. **Check Transaction Successful**: The software verifies if the user's payment is sufficient to purchase the selected coffee and completes the transaction accordingly.

5. **Make Coffee**: The software prepares the selected type of coffee by deducting the required resources from the machine and delivering the coffee to the user.

## Usage

To run the coffee machine software, execute the `source_code.py` file. The software provides a user-friendly command-line interface for interaction. You can type the following commands:

- `espresso`: Make an espresso coffee.
- `latte`: Make a latte coffee.
- `cappuccino`: Make a cappuccino coffee.
- `report`: Generate a report of the coffee machine status.
- `off`: Turn off the coffee machine.

If you need assistance or want to explore other commands, you can type `help` to access the help section.

## Project Structure

The project consists of the following files:

1. `source_code.py`: The main source code file that contains the coffee machine software logic. It imports functions from `prog_functions.py` and uses ASCII art from `art.py` for UI enhancements.

2. `prog_functions.py`: This file provides additional functions required by the coffee machine software, including functions to read the company's profit, generate reports, process payments, and handle the coffee purchase process.

3. `database.py`: This file defines a dictionary that stores the menu options, including the available types of coffee, their ingredients, and costs. It also defines another dictionary for tracking the available resources in the coffee machine.

4. `art.py`: This file contains ASCII art used for enhancing the user interface. It includes the company logo, report design, and payment section design.

## Credits

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy

The ASCII art used in the software's user interface is created using the `art` library.

Note: The ASCII art in the README might not render properly on all platforms. Please refer to the actual source code files for accurate representations.

Feel free to explore the source code and adapt it to your needs. Enjoy your coffee machine software!


## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.



## Contact
- Author: [Ehiane Oigiagbe(me)](https://github.com/ehiane)
  <p align="left">
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
  </p>
