import os
#Create a letter using starting_letter.txt  ##DONE
#for each name in invited_names.txt ##DONE
#Replace the [name] placeholder with the actual name. ##DONE
#Save the letters in the folder "ReadyToSend". ##DONE
    


NAME_FILE= "./emailAutomation/Input/Names/invited_names.txt"
TEMPLATE = "./emailAutomation/Input/Letters/starting_letter.txt"
SAVE_PATH = "./emailAutomation/Output/ReadyToSend/";


def get_names(file):
    """
    opens the file and gets the names inside the file, line by line.
    """
    names = []; 
    with open(file) as source:
        lines = source.readlines();
        for line in lines:
            name = line.strip("\n");
            names.append(name);
    
    return names;



receipients = get_names(NAME_FILE); #a list of names to send the mail to.

def generate_letter(name, user_name, template_file, new_file):
    """
    grabs contents of the template file, 
    \nedits it line by line and prints
    it's content to a new file in the a specific path.  
    """

    file_contents = "";
    with open(template_file) as file:
        lines = file.readlines();
        for line in lines:
            line = line.replace("[name]",name);
            line = line.replace("Angela", f"{user_name}")
            file_contents += line; 
       
    # changing the newfile's path to the destination of the correct file path 
    new_file = SAVE_PATH+new_file;
    
    # writing the corrected contents to each file.
    with open(new_file, "w") as new:
        new.write(file_contents);


for name in receipients:
    generate_letter(name,"Ehiane", TEMPLATE, new_file=f"{name}_letter.txt");