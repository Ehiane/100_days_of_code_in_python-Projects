
#Requirements:
"""
    *attributes: question_number = 0(by default), question_list
    *method: next_question();
"""
class QuizBrain:
    def __init__(self,  question_list):
        self.question_number = 0;
        self.question_list = question_list;
        self.score = 0;
    
    
    def still_has_questions(self):
        """
        returns True if questions remain, else returns False.
        """
        return len(self.question_list) > self.question_number;

    def next_question(self):
        """
        collects answers per question from the question_list, checks if it wrong or right.
        """
        user_question = self.question_list[self.question_number].text;
        user_response = input(f"Q.{self.question_number +1}: {user_question} (True/False)?: ");
        
        if self.is_correct(user_response):
            print("You got it right!")
            self.score += 1;
            self.print_score();
        else:
            print("You got it wrong!")
            print(f"The correct answer is {self.question_list[self.question_number].answer}.")
            self.print_score();
        
        self.question_number += 1;

    
    def is_correct(self,response):
        return True if self.question_list[self.question_number ].answer.lower() == response.lower() else False;

    def print_score(self):
        print(f"Your current score is {self.score}/{self.question_number +1}\n")