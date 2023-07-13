# OOP Quiz Game

This project is a simple quiz application that tests your knowledge with a set of True/False questions. The program presents each question one by one, allows you to answer, and provides feedback on whether your answer was correct or incorrect. At the end of the quiz, it displays your final score.

## Getting Started

To run the quiz application, make sure you have the following files in your project directory:

- main.py
- question_model.py
- quiz_brain.py
- data.py

## Prerequisites

The project requires Python 3.x to be installed on your system. If you don't have Python installed, you can download it from the official Python website: python.org.

## Running the Quiz

To run the quiz, execute the `main.py` file using the Python interpreter. Open a terminal or command prompt, navigate to the project directory, and enter the following command:

```shell
python main.py
```

The quiz will start, and you'll be presented with True/False questions one by one. Enter your answer by typing either "True" or "False" and pressing Enter. After each answer, the program will provide feedback on whether your answer was correct or incorrect.

At the end of the quiz, the program will display your final score.

## Customizing the Quiz Questions

The quiz questions are stored in the `data.py` file. The file contains a list of dictionaries, where each dictionary represents a question. You can modify the existing questions or add new ones by following the same format. Each question dictionary should have the following keys:

- `category` (string): The category of the question.
- `type` (string): The type of the question (in this case, "boolean").
- `difficulty` (string): The difficulty level of the question.
- `question` (string): The actual question text.
- `correct_answer` (string): The correct answer ("True" or "False").
- `incorrect_answers` (list of strings): Incorrect answer options.

Modify the `question_data` list in `data.py` to add, remove, or modify the quiz questions.

## Project Files

### `main.py`

This file is the entry point of the application. It imports the necessary modules (`data`, `question_model`, and `quiz_brain`) and sets up the quiz. It creates a list of question objects, initializes a `QuizBrain` object, and starts the quiz loop. After the quiz ends, it displays the final score.

### `question_model.py`

This file contains the `Question` class, which represents a single question in the quiz. Each question object has a `text` attribute (the question text) and an `answer` attribute (the correct answer).

### `quiz_brain.py`

This file contains the `QuizBrain` class, which manages the quiz flow and keeps track of the question number, question list, and score. It has methods for checking if there are remaining questions, displaying the next question, checking if the answer is correct, and printing the current score.

### `data.py`

This file stores the quiz questions in the `question_data` list. Each question is represented as a dictionary with various attributes, such as category, type, difficulty, question text, correct answer, and incorrect answer options.

## Acknowledgments

The quiz questions used in this project are sourced from an API provided by [opentdb.com](https://opentdb.com/). The `question_data` list in `data.py` contains a sample set of questions for demonstration purposes.

Feel free to modify the project files, customize the questions, and expand the functionality as per your requirements.

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy



Happy quizzing!

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
