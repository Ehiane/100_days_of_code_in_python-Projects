![email-gif-1200](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/abcb7159-ba45-4bcd-8aef-b6ce4b9b9677)

# Automated Letter Generation

This Python script generates personalized letters by replacing placeholders in a template with names from a given list. It reads the list of names from `invited_names.txt`, uses a starting letter template from `starting_letter.txt`, replaces the `[name]` placeholder with the actual name, and saves the personalized letters in the "ReadyToSend" folder.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your system.

## Getting Started

1. Clone or download this repository to your local machine.

2. Navigate to the project directory containing the Python script and input files.

3. Create two input files inside the `Input` directory:

   - `Names/invited_names.txt`: This file should contain a list of names, each on a separate line, to whom you want to send the personalized letters.

   - `Letters/starting_letter.txt`: This file should contain the starting letter template, with the `[name]` placeholder where the recipient's name will be inserted.

4. Create an empty folder named "ReadyToSend" inside the `Output` directory. The script will save the generated letters in this folder.

## How to Use

To generate the personalized letters, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Execute the following command to run the script:

   ```bash
   python letter_generator.py
   ```
The script will read the list of names from invited_names.txt and the template from starting_letter.txt. It will then generate a personalized letter for each name, replace the [name] placeholder with the actual name, and save the letters as individual files in the "ReadyToSend" folder.

After the script finishes execution, you will find the personalized letters inside the "ReadyToSend" folder.


## Customization
You can modify the starting letter template in starting_letter.txt to include other placeholders that you want to replace. Make sure to update the script accordingly to handle these placeholders.

You can also change the user name used in the letter generation by modifying the generate_letter function in the script.


## Credits

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy


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
