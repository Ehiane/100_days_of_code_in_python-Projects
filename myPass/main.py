# $ Imports(s):
from tkinter import *  # only imports classes but not regular functions
from tkinter import messagebox as m
from random import randint, shuffle, choice
import pyperclip

#!responsible for copying to clipboard
import json

# %Global(s):
LOGO = "logo.png"
DATABASE = "data.json"
FONT = ("Courier", 12)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
#! List Comprehension(choice, randint, shuffle --all from random module).


def generate_password():
    letters = [chr(x) for x in range(ord("a"), ord("z") + 1)] + [
        chr(x) for x in range(ord("A"), ord("Z") + 1)
    ]  # the alphabet in lower and higher case using list comprehension.
    numbers = [str(x) for x in range(10)]  # number from 1 - 10 using list comprehension
    symbols = [
        chr(x) for x in [33, 35, 36, 37, 38, 40, 41, 42, 43]
    ]  # converting ascii characters of symbols to characters using list comprehension. ;

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, string=password)
    # once clicked, it will populate the entry with generated password;

    pyperclip.copy(password)
    #!Copy's the password to my clipboard.


# print(f"Your password is: {password}");
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_prog_data():
    website, email_username, password = (
        website_input.get(),
        userID_input.get(),
        password_input.get(),
    )

    if website == "" or password == "":
        m.showinfo(title="Error!", message="Please don't leave any field empty!")
    else:
        #! using json format.
        new_data = {
            website: {
                "email": email_username,
                "password": password,
            }
        }
        return new_data


def clear_entries():
    website_input.delete(0, END)
    password_input.delete(0, END)


#! .load() -> python(dict) 
def save_to_file(filename=DATABASE):
    user_data = save_prog_data()
    if user_data != None:
        # open the file and see if there's anything in side
        try:
            with open(filename, "r") as file:
                new_data = json.load(file)
                print("test1: trying to read data")

                if new_data != None:
                    # if file is found, update the file with the new data.
                    print(new_data)
                    print("test2: trying to update the data")
                    with open(filename, "w") as file:
                        json.dump(new_data, file, indent=4)
                        print(
                            "test3: added updated data to the file.\n*******************"
                        )
                    m.showinfo(
                        title="Password Manager", message="Successfully Saved Info!"
                    )

        # if file not found, create a new file and dump the old data there
        except FileNotFoundError:
            print("test1.1: couldn't read data")
            with open(filename, "w") as file:
                json.dump(user_data, file, indent=4)
                print("test1.2: creating new file\n*******************")
            m.showinfo(title="Password Manager", message="Successfully Saved Info!")

        # if file found but empty, create a new file and dump the old data there
        except json.decoder.JSONDecodeError:
            print("test1.11: couldn't read data")
            with open(filename, "w") as file:
                json.dump(user_data, file, indent=4)
                print("test1.12: creating new file\n*******************")
            m.showinfo(title="Password Manager", message="Successfully Saved Info!")

        # Regardless of the outcome, do this:
        finally:
            # clearing unwanted entries.
            clear_entries()

    else:
        print("couldn't save to file")

# ---------------------------- SEARCH ------------------------------- #
def search_file(filname = DATABASE):
  
    try:
        with open(filname, "r") as file:
            data_copy = json.load(file); #data_copy is in dict form now
    except FileNotFoundError:
        m.showinfo(title="error", message="No Data file found.");
    except json.decoder.JSONDecodeError:
        m.showinfo(title="error", message="Data file is empty");
    else:
        query = website_input.get();
        query_email = data_copy[query]['email'];
        query_password = data_copy[query]['password'];
        m.showinfo(title=query, message=f"email: {query_email} \npassword: {query_password} ");
    finally:
        clear_entries();



    pass;


# ---------------------------- UI SETUP ------------------------------- #
##Window setup:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

##Canvas Setup:
canvas = Canvas(width=200, height=200)

# *creating image_object;
logo_obj = PhotoImage(file=LOGO)

canvas.create_image(100, 100, image=logo_obj)

##Label(s):
website_label = Label(text="Website:", font=FONT)
userID_label = Label(text="Email:", font=FONT)
password_label = Label(text="Password:", font=FONT)

##Entry(s):
website_input = Entry(width=35, justify="left")
userID_input = Entry(width=35, justify="left")
password_input = Entry(width=21, justify="left")
userID_input.insert(
    0, "user@email.com"
)  # *END is a constant that represents the very last character of the entry, 0 is the beginnig

website_label.focus()
#! Sets the cursor to this entry at the start of the program.


##Button(s):
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_to_file)
search_button = Button(text="Search", command=search_file, width=15);


## Element positioning:
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1,padx=0,pady=0)
website_input.grid(column=1, row=1, columnspan=2,padx=0,pady=0)
userID_label.grid(column=0, row=2,padx=0,pady=0)
userID_input.grid(column=1, row=2, columnspan=2,padx=0,pady=0)
password_label.grid(column=0, row=3,padx=0,pady=0)
password_input.grid(column=1, row=3,padx=0,pady=0)
# Update the grid position
generate_password_button.grid(column=2, row=3,padx=0,pady=0)
add_button.grid(column=1, row=4, columnspan=2,padx=0,pady=0)
search_button.grid(column=3, row=1,padx=0,pady=0);


window.mainloop()

"""
# tried to import the passwordManager folder: it worked.
# import sys
# import os

# # Add the path to the root directory (folder of folders) to sys.path
# root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(root_directory)

# # Now you can import the module
# from passwordGenerator.complexPasswordGenerator import random_password_generator
"""
