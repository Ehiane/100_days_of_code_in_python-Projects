import helperFunctions as Help

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

    #list comprehension:
    # even_nums = [x for x in range(1,101) if x%2 ==0] #gives a list of even numbers from 1-100 in a
    # print(even_nums);
    # n = int(input("Check this number: "))
    # prime_checker(number=n)
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    # encrypt(text, shift)

    # caesar(start_text=text, shift_amount=shift, cipher_direction=direction);

    # to wipe an existing dictionary you can just set it to {} and it'll automatically wipe it. 
    travel_log = {
        "Nigeria": {"Visited States": ["Edo", "PortHarcourt","Lagos", "Ogun", "Ibadan"], "Homes": ["Lagos","PortHarcourt","Edo"]},
        "United States": {"Visited States": ["California","Indianapolis", "Washington", "Washington DC", "Pennsylvania", "Maryland"], "Homes":["Washington", "Maryland","Pennsylvania", "Indianapolis"]}
    };
    
    def printNestedDictList(dictionary, indent=0):
        """
        prints out a nested dictionary, where the values of the nested dictionary is a list.
        """
        if(isinstance(dictionary, dict)):
            for key, value in dictionary.items():
                    print(f"{ ' '*indent}{key}:");
                    printNestedDictList(value, indent + 4);
        
        elif(isinstance(dictionary, list)):
            print(f"{' ' * indent}: {', '.join(dictionary)}");

    printNestedDictList(travel_log);

main();