"""
REQUIRMENTS:

*Should hold the following attributes: text, answer
    e.g. {var} = {class}("{text}", "{answer}")
"""

class Question:
    def __init__(self, text, answer):
        self.text = text;
        self.answer = answer;

#object instantiation;
# question1 = Question("There are 26 letters in the Alphabet", "False")

# print(question1.text);
