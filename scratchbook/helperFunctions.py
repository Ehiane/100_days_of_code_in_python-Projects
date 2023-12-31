#Things to watch out for:
# '/' - float division, '//' integer division
#Order of priority: P_E_MD_AS_LR
# print(3+3*3/3-3);
# round function helps a lot

# 1 year = 365 days
#        = 52 weeks
#        = 12 months



import random as r

import math as m

bug = "🐞";

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

max_shift = len(alphabet)


def calcAgeto90(currentAge):
    """
    get user's current age, subtract from 90, to get years left, 
    convert the age in years to days, months and weeks
    """
    WEEKS = 52;
    DAYS = 365;
    MONTHS = 12;

    age_in_years = int(currentAge);
    years_left = 90 - age_in_years;

    #converting to weeks:
    weeks_left = years_left * WEEKS;
    days_left = years_left * DAYS;
    months_left = years_left * MONTHS;

    return days_left, weeks_left, months_left;

def tip_calculator(bill):
  custom_tip = int(input("How much tip would you like to give? 10, 12, or 15?"));
  custom_tip= 1 + custom_tip/100;
  tip_w_bill = bill * custom_tip;
  split_amount = int(input("How many people to split the bill? "));
  split_amount = tip_w_bill/split_amount;
  bill_per_person = round(split_amount, 2);
  return bill_per_person;

def calc_bmi(height, weight):
  user_bmi = weight / height**2;
  user_bmi = round(user_bmi, 2);
  return user_bmi;

def determine_bmi(height, weight):
    user_bmi = calc_bmi(height, weight);
    if user_bmi < 18.5:
        print(f"Your BMI is {user_bmi}, you are underweight");
    elif user_bmi >= 18.5 and user_bmi < 25:
        print(f"Your BMI is {user_bmi}, you have a normal weight");
    elif user_bmi >= 25 and user_bmi < 30:
        print(f"Your BMI is {user_bmi}, you are slightly overweight.");
    elif user_bmi>= 30 and user_bmi < 35:
        print(f"Your BMI is {user_bmi}, you are obese.");
    elif user_bmi >= 35:
        print("Your BMI is {user_bmi}, you are clinically obese.")

def checkExtra(size, pepperoni, cheese):
    extra_bill = 0
    is_pepperoni = True if pepperoni == "Y" else False;
    is_cheese = True if cheese == "Y" else False;
    
    if is_pepperoni == True and is_cheese == True:
        if(size == "M" or size == "L"):
            extra_bill += 3;
        else:
            extra_bill += 2; #for pepperoni
            extra_bill +=1; #for cheese

    elif is_pepperoni == False and is_cheese == True:
        extra_bill += 1;

    elif is_pepperoni == True and is_cheese == False:
        if(size == "M" or size == "L"):
            extra_bill += 3;
        else:
            extra_bill += 2;
    else:
        pass;

    return extra_bill;
    
def pizzaBill(size, pepperoni, cheese):
    bill = 0;

    if size == "S":
        bill = 15;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");

    elif size == "M":
        bill = 20;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");
    elif size == "L":
        bill = 25;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");

def loveCalc(name1, name2):
    name1,name2 = name1.lower(),name2.lower();
    #truelove
    t_tally = name1.count("t") + name2.count("t");
    r_tally = name1.count("r") + name2.count("r");
    u_tally = name1.count("u") + name2.count("u");
    e_tally = name1.count("e") + name2.count("e");
    first_score = t_tally + r_tally + u_tally + e_tally;

    l_tally = name1.count("l") + name2.count("l");
    o_tally = name1.count("o") + name2.count("o");
    v_tally = name1.count("v") + name2.count("v");
    second_score = l_tally + o_tally +v_tally +e_tally;

    #convert to string
    first_score, second_score = str(first_score), str(second_score);
    total_score = first_score + second_score;
    total_score = int(total_score);
    return total_score;


def prime_checker(number):
    #THOUGHT PROCESS:  check if n is a multliple of any integer between 2 and sqrt(n) gotten from the trial division concept.
    end =  round(m.sqrt(number)+1); #+1 was to include the last number.
    is_prime = True; #default set to true.

    if number == 2:
        print("It's a prime number"); 

    for i in range(2, end): #using my thought process 
        if number%i == 0:
            is_prime = False;
        
        if is_prime == False:
            print("It's  not a prime number");
            break;
        if is_prime == True :
            if end == 2 or i == end-1: #end ==2 was to keep track of the range for numbers like 3 and 5.
                print("It's a prime number")

                
def encrypt(text, shift):
    response = "";
    for i in range(len(text)):
        conversion = ord(text[i]) + shift
        response += chr(conversion)
    print(response)


def caesar(start_text, shift_amount, cipher_direction):
    play_on = True
    while play_on == True:
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char not in alphabet:
                end_text += char
                continue
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        print(f"Here's the {cipher_direction}d result: {end_text}")

        decsion = input("Do you want to keep playing? [yes or no]\n>>").lower()
        if decsion == "yes":
            start_text = input("Type your new message:\n").lower();
            shift_amount = int(input("Type your new shift number:\n"));
            cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
            if shift_amount > max_shift:
                shift_amount %= max_shift
        
        elif decsion == "no":
            play_on = False



# #-1: Import and print the logo from art.py when the program starts.

# #-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# max_shift = len(alphabet)
# if shift > max_shift:
#     shift %= max_shift

#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
