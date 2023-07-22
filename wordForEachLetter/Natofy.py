import pandas

#! NATOFY: to use other words to clarify a letter that has been said:
#! example: A- Apple, B- Ball, etc  

# !THERE'S PROBABLY A MORE EFFICIENT WAY OF DOING THIS:
def filter_database(database) -> dict:
    """
    refines the pandas dataframe into an actual dictionary without using read_toDict();
    """
    phonetic_dict = {row.letter: row.code for (index, row) in database.iterrows()}
    return phonetic_dict;



def natofication(local_db) -> None:
    """
    uses user input to get the natofied words for each letter in the prompt
    """
    word_to_natofy = input("Insert the word you want to NATOFY: ").upper();
    word_to_natofy = word_to_natofy.replace(" ", "");
    print(word_to_natofy);
    for letter in word_to_natofy:
        natofied_word = local_db[letter];
        print(f"{letter} for {natofied_word}")


def run_program():
    #SECTION: 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
        # Step1.1: get access of the database as a dataframe.
    database = pandas.read_csv("nato_phonetic_alphabet.csv");
    local_database = filter_database(database);
    
    #SECTION: 2. Create a list of the phonetic code words from a word that the user inputs.
    natofication(local_db= local_database);
    pass;

run_program();