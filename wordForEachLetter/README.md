# 🔤🎰 |WordForEachLetter - NATOFICATION
<img width="500" alt="image" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/eaac59ac-2920-44cb-945a-c41798690e72">


![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)

## Introduction

Natofy is a Python script that allows users to convert words into their corresponding NATO phonetic alphabet representation. The NATO phonetic alphabet is a system used to clarify letters that may be easily misunderstood when communicated verbally. For example, "A" is represented as "Alfa," "B" as "Bravo," and so on, I made use of Dictionary comprehension to manually convert the .csv file to a dictionary.

## How It Works

The script takes advantage of a local database containing the NATO phonetic alphabet codes for each letter. It performs the following steps to natofy a given word:

1. Read the NATO phonetic alphabet codes from the CSV database into a dictionary.
2. Prompt the user to input a word they want to natofy.
3. Remove any spaces from the user input and convert it to uppercase.
4. For each letter in the word, look up the corresponding NATO phonetic code from the dictionary and display it.

## Requirements

- Python 3.x
- Pandas library: Install using `pip install pandas`

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/natofy.git
```
2. Navigate to the project directory:
```
cd  WordForEachLetter
```
3. Install the required dependencies:
```
pip install pandas
```

## Usage

1. Create a CSV file named "nato_phonetic_alphabet.csv" with the NATO phonetic alphabet codes. The file should have columns "letter" and "code" containing the letters and their respective NATO codes.

<img width="227" alt="image" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/343bb4b3-dc77-48f3-8637-011a42c0c095">



2. Run the Python script:
```
python Natofy.py
```

3. Input the word you want to natofy when prompted by the script.

4. The script will display the NATO phonetic code for each letter in the input word.


## Credits

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>

