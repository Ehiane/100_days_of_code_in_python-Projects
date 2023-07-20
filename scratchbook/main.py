import helperFunctions as Help
import csv;


# from turtle import Turtle, Screen
# from prettytable import PrettyTable



## TURTLE CLASS
#making use of Turtle class and saving it to an object
# timmy_turtle = Turtle()

# #changing the shape
# print(timmy_turtle);
# timmy_turtle.shape("turtle")

# my_screen = Screen(); 
# print(my_screen.canvheight);


# #coloring the turtle
# timmy_turtle.fillcolor("cyan");

# #moving the position of the turtle.
# timmy_turtle.forward(100);


# my_screen.exitonclick();


# #Pretty Table class
# table = PrettyTable();

# table.field_names = ["Name", "Club", "Position", "Nationality", "Number"];
# table.add_rows( [
#     ["Jude Bellingham", "Real-Madrid", "CM", "England", "22" ],
#     ["Bukayo Saka", "Arsenal", "RW", "England", "7"],
# ])
# table.add_row(["","","","",""],divider=True);
# table.add_row(["Moussa Diaby", "Bayer-04", "RW", "France", "19" ]);
# table.add_row(["Kylian Mbappe", "Paris-Saint-German(PSG)", "ST","France", "7"]);

#challenge
# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charamander"], align="l");
# table.add_column("Type",["Electric", "Water", "Fire"], align="l");

# print(table);


#calculator essentials:


# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# #create a dictionary to hold all these operations

# ##possible through mapping the functions signature .
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }

# do = operations["+"]
# do(2, 3)

# #Opening Files.
# file = open("external.txt");
# contents = file.read(); #returns the content of the file as a string.
# print(contents);

# essential to free up the resources of the computer.
# file.close();


# with the "with" keyword, there's no need to manually close the file, the functions
# handles that scenario by checking exactly when we are done manipulating with the file.
# modes: 
"""
a : append
w: clears then writes
"""

# if file mentioned is non-existent, 
# python will make the file for you.
# with open("external.txt", mode= "a") as file:
#     file.write("\nNew text");

    # contents = file.read();
    # print(contents);




# def read_csv(file_name):
#     temps = [];
#     with open(file_name) as file:
#       data = csv.reader(file);
#       for row in data:
#         # print all the temoeratures
#         if row[1] != "temp":
#           temp = int(row[1]);
#           temps.append(temp);
        
#         # print(row);
#       print(temps)


def main():
  # age = input("What is you current age? ");
  # [days_remaining, weeks_remaining,months_remaing] = calcAgeto90(age);
  # print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaing} months left.");

  # print("\n-------------------------------[next function]-----------------------------------\n")

  # total_bill = float(input("What was your total bill? "));
  # each_person_pay = tip_calculator(total_bill);
  # print(f"Each person should pay: ${each_person_pay}");
  # height = float(input("enter your height in m: "))
  # weight = float(input("enter your weight in kg: "))
  # determine_bmi(height, weight);
  # print("\n-------------------------------[next function]-----------------------------------\n")

  # print("Welcome to Python Pizza Deliveries!")
  # size = input("What size pizza do you want? S, M, or L ")
  # add_pepperoni = input("Do you want pepperoni? Y or N ")
  # extra_cheese = input("Do you want extra cheese? Y or N ")
  # pizzaBill(size, add_pepperoni, extra_cheese);
#   print("Welcome to the Love Calculator!")
#   name1 = input("What is your name? \n")
#   name2 = input("What is their name? \n")


  # print(data);
  # read_csv("weather_data.csv");

  #----------------------[]---------------------------------------
#   score = loveCalc(name1, name2);
#   if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.");
#   elif score >= 40 and score <=50:
#     print(f"Your score is {score}, you are alright together.");
#   else:
#     print(f"Your score is {score}.");

    # fruits = ["apple","cherry","mango"];
    # vegetables = ["celery", "potatoes", "tomatoes"];
    # fruits_veg = [fruits,vegetables];
    # print(fruits_veg);
#-----------------------------------------------------------[]--------------------------------------
    #list comprehension:
    # even_nums = [x for x in range(1,101) if x%2 ==0] #gives a list of even numbers from 1-100 in a
    # print(even_nums);
    # n = int(input("Check this number: "))
    # prime_checker(number=n)
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    # encrypt(text, shift)

#--------------------------------------------------[]------------------------------------
    # caesar(start_text=text, shift_amount=shift, cipher_direction=direction);

    # to wipe an existing dictionary you can just set it to {} and it'll automatically wipe it. 
    # travel_log = {
    #     "Nigeria": {"Visited States": ["Edo", "PortHarcourt","Lagos", "Ogun", "Ibadan"], "Homes": ["Lagos","PortHarcourt","Edo"]},
    #     "United States": {"Visited States": ["California","Indianapolis", "Washington", "Washington DC", "Pennsylvania", "Maryland"], "Homes":["Washington", "Maryland","Pennsylvania", "Indianapolis"]}
    # };
    
    # def printNestedDictList(dictionary, indent=0):
    #     """
    #     prints out a nested dictionary, where the values of the nested dictionary is a list.
    #     """
    #     if(isinstance(dictionary, dict)):
    #         for key, value in dictionary.items():
    #                 print(f"{ ' '*indent}{key}:");
    #                 printNestedDictList(value, indent + 4);
        
    #     elif(isinstance(dictionary, list)):
    #         print(f"{' ' * indent}: {', '.join(dictionary)}");

    # printNestedDictList(travel_log);

  ## OOP Notes:
    #* you can instantiate attributes of classes outside of a class block. for instance
    
    # """
    # class User:
    #   pass;
    
    # public_user = User();
    # public_user.name = "fred meyer"
    # public_user.age = 17; 

    # print(public_user) #[]"fred meyer", 17];
    # """
      
  pass;

main();