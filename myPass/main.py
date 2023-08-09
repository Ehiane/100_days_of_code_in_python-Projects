# tried to import the passwordManager folder: it worked.
# import sys
# import os

# # Add the path to the root directory (folder of folders) to sys.path
# root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(root_directory)

# # Now you can import the module
# from passwordGenerator.complexPasswordGenerator import random_password_generator

from tkinter import * #only imports classes but not regular functions 
from tkinter import messagebox as m;
import random;


# %Global(s):
LOGO = "logo.png"
DATABASE = "data.txt";
FONT = ("Courier",12);
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10);
nr_symbols = random.randint(2, 4);
nr_numbers = random.randint(2, 4);

# List Comprehension.
password_list =  [random.choice(letters) for char in range(nr_letters)];
password_list += [random.choice(symbols) for symb in range(nr_symbols)];
password_list += [random.choice(numbers) for num in range(nr_numbers)];


random.shuffle(password_list);

password = "";
for char in password_list:
  password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_prog_data():
    website,email_username,password = website_input.get(), userID_input.get(), password_input.get();
    
    if website == "" or password == "":
        m.showinfo(title="Error!", message="Please don't leave any field empty!");
    else:
        pop_up_messg = f"These are the details entered: \nEmail: {email_username}\nPassword: {password} \nIs it ok to save?";
        # verifiying if user is satisfied with given details.
        is_okay = m.askokcancel(title=website, message=f"{pop_up_messg}")
        if is_okay:
            return website,email_username, password;


def clear_entries():
    website_input.delete(0,END);
    password_input.delete(0,END);


def save_to_file(filename = DATABASE):
    user_data = save_prog_data(); 
    if user_data != None:
        content = f"{user_data[0]} | {user_data[1]} | {user_data[2]}\n";
        # write to file
        with open(filename, "a") as file:
            file.write(content);
            m.showinfo(title="Password Manager", message="Successfully Saved Info!");
        # clearing unwanted entries.
        clear_entries();
    else:
        print("couldn't save to file");


# ---------------------------- UI SETUP ------------------------------- #
##Window setup:
window = Tk();
window.title("Password Manager")
window.config(padx=50, pady= 50)

##Canvas Setup:
canvas = Canvas(width=200, height= 200);

#*creating image_object;
logo_obj = PhotoImage(file=LOGO);

canvas.create_image(100,100, image= logo_obj);

##Label(s):
website_label = Label(text="Website:",font= FONT);
userID_label = Label(text="Email/Username:", font=FONT);
password_label = Label(text="Password:",font= FONT);

##Entry(s):
website_input = Entry(width=35,justify="left");
userID_input = Entry(width=35,justify="left");
password_input= Entry(width=21,justify="left");
userID_input.insert(0, "ehis.oigigagbe@gmail.com") #*END is a constant that represents the very last character of the entry, 0 is the beginnig

website_label.focus(); #! Sets the cursor to this entry at the start of the program.


##Button(s):
generate_password_button = Button(text="Generate Password"); #add command
add_button= Button(text="Add", width=36,command=save_to_file); #add command


##Element positioning:
canvas.grid(column=1, row=0);
website_label.grid(column=0, row=1);
website_input.grid(column=1, row=1, columnspan=2);
userID_label.grid(column=0, row=2);
userID_input.grid(column=1, row=2, columnspan=2);
password_input.grid(column=1, row=3);
password_label.grid(column=0,row=3);
generate_password_button.grid(column=2,row=3);
add_button.grid(column=1, row=4, columnspan=2);



window.mainloop();