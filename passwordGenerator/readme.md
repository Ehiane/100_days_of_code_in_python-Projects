# Random Password Generator

## Demo
<img width="559" alt="image" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/fc4bd0c7-be6b-47ab-a6c9-d47930397057">

This Python program generates a random password based on user-specified criteria. The generated password includes a combination of letters, symbols, and numbers.

## Requirements

To run this program, make sure you have Python 3. {...} installed on your system.

## Getting Started

1. Clone the repository or download the Python script file.

2. Open a terminal or command prompt and navigate to the directory where the script file is located.

3. Run the following command to start the program:

   ```shell
   python random_password_generator.py
   ```

## How to Use

1. Upon running the program, the program's logo will be displayed.

2. You will be prompted to enter the following information:

   - **Number of letters:** Specify the desired number of letters in the password.
   - **Number of symbols:** Specify the desired number of symbols in the password.
   - **Number of numbers:** Specify the desired number of numbers in the password.

3. Once you provide the required information, the program will generate a random password based on the specified criteria.

4. The generated password will be displayed on the screen.

5. Feel free to use the generated password for your desired purposes.

## List Comprehension

The program utilizes the power of list comprehension to generate the character options for the password generation:

- **Letters:**

  The `letters` list is generated using the following list comprehension code:

  ```python
  letters = [chr(x) for x in range(ord('a'), ord('z')+1)] + [chr(x) for x in range(ord('A'), ord('Z')+1)]
  ```

  This code iterates over the ASCII values corresponding to lowercase and uppercase letters and uses `chr(x)` to convert each ASCII value to its corresponding character. The resulting characters are added to the `letters` list using list concatenation.

- **Numbers:**

  The `numbers` list is generated using the following list comprehension code:

  ```python
  numbers = [str(x) for x in range(10)]
  ```

  This code iterates over the range of numbers from 0 to 9 and converts each number to a string using `str(x)`. The resulting strings are added to the `numbers` list.

- **Symbols:**

  The `symbols` list is generated using the following list comprehension code:

  ```python
  symbols = [chr(x) for x in [33, 35, 36, 37, 38, 40, 41, 42, 43]]
  ```

  This code uses list comprehension to convert a list of ASCII values representing symbols to their corresponding characters. The resulting characters are added to the `symbols` list.

## Logo

The program's logo is displayed using ASCII art. It adds a visual element to the program and enhances the user experience.



## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>

## Author

This random password generator was created by [Ehiane Oigiagbe(me)](https://github.com/ehiane).

Feel free to modify or customize the program as per your requirements. Enjoy generating random passwords for your needs!
