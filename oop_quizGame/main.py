from data import question_data;
from question_model import Question;
from quiz_brain import QuizBrain;

logo = """
 ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  
██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                     
                                                                     
"""
#initialise a list of question objects using question class and the data file.
question_bank = [];

for i in range(len(question_data)):
    text = question_data[i]['question'];
    answer = question_data[i]['correct_answer'];
    question_bank.append(Question(text,answer));

#now quaestion bank is a list of questions.
# print(list_of_questions[len(question_data) -1].text); this was to verify that it works.

#now that we have that running we have some TODO 's to handle
#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

quiz = QuizBrain(question_bank);

print(logo);
while(quiz.still_has_questions()):
    quiz.next_question();

print(f"You've completed the quiz\nYour final score is {quiz.score}/{len(quiz.question_list)}")