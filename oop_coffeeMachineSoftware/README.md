# ☕🤖 [OOP] | "OOP Version" Coffee Machine Software

This repository contains the source code for a coffee machine software in `Object oriented Programming style` . The software allows users to interact with the coffee machine, make various types of coffee, check resources, process payments, and generate reports.

Here is the sequential programming version of this project(without OOP) [base_mode](https://github.com/Ehiane/100_days_of_code_in_python-Projects/tree/main/coffeeMachineSoftware)

## Demo
![bean-haven demo gif](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5c0a02e9-bc82-47d0-a652-67deb7f96fe7)

## Program Requirements

The coffee machine software fulfills the following requirements:

1. `generate_report`: Users can generate a report that displays the current status of the coffee machine, this function accepts a coffee_maker object as it's input.

2. `find_drinkObject`: The software makes use of this function to assign the user's choice of drink an object that represents the drink in the program. Accepts the prompt and a dictionary of all objects.

3. `run_software`: This is the function responsible for all the operations within the program.




## Usage

To run the coffee machine software, execute the `main.py` file. The software provides a user-friendly command-line interface for interaction. You can type the following commands:

- `espresso`: Make an espresso coffee.
- `latte`: Make a latte coffee.
- `cappuccino`: Make a cappuccino coffee.
- `report`: Generate a report of the coffee machine status.
- `off`: Turn off the coffee machine.

If you need assistance or want to explore other commands, you can type `help` to access the help section.

## Project Structure

The project consists of the following files:

1. `main.py`: The main source code file that contains the coffee machine software logic. It imports the  `menuItem`, `CoffeeMaker`, `MoneyMachine` and `SystemGraphics` classes inorder to access the user's requests within the software.  

2. `UI_interactions.py `: This file provides additional functions required by the coffee machine software that handles the Software's UI handle the coffee purchase process.

3. `coffee_maker.py`: This file contains the `CoffeeMaker` class, which serves as a blueprint for any internal info regarding the specific drink.
   
4. `menu.py`: This file contains the `MenuItem` and `Menu` classes. Both classes act as a blueprint for the structure of a coffee object. The `Menu` class' `find_drink(self, order_name)` function returns the specifc drink with all it's ingredients to an object `MenuItem`, which makes the object accessible.
   
5. `money_machine.py`: This file contains all the necessary functions regarding the transactional side of the software.
   
6. `graphics.py`: This file contains ASCII art used for enhancing the user interface and the graphics class `SystemGraphics` responsible for implenting system graphics within the software. It includes the company logo, report design, and payment section design.



## Credits

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project and supplying the base implementations for `CoffeeMaker` `Menu` `MenuItem` `MoneyMachine` through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy

The ASCII art used in the software's user interface is created using the `art` library.

Note: The ASCII art in the README might not render properly on all platforms. Please refer to the actual source code files for accurate representations.

Feel free to explore the source code and adapt it to your needs. Enjoy your coffee machine software!


## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.



## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>


