import random as r
"""
Understanding 
In this list comprehension below 👇, chr(x) is used to convert the ASCII value x to its corresponding character. 
The range for lowercase letters is obtained using ord('a') and ord('z'), 
while the range for uppercase letters is obtained using ord('A') and ord('Z').
By iterating over these ranges and converting each ASCII value to a character, we can generate the desired list of letters.
"""
letters = [chr(x) for x in range(ord('a'), ord('z')+1)] + [chr(x) for x in range(ord('A'), ord('Z')+1)] #the alphabet in lower and higher case using list comprehension.


numbers = [str(x) for x in range(10)] #number from 1 - 10 using list comprehension

symbols = [chr(x) for x in [33, 35, 36, 37, 38, 40, 41, 42, 43]] #converting ascii characters of symbols to characters using list comprehension. ;

print("👇");


logo = """
 ____                                                      __      ____                                          __                   
/\  _`\                                                   /\ \    /\  _`\                                       /\ \__                
\ \ \L\ \ __      ____    ____  __  __  __    ___   _ __  \_\ \   \ \ \L\_\     __    ___      __   _ __    __  \ \ ,_\   ___   _ ____  
 \ \ ,__/'__`\   /',__\  /',__\/\ \/\ \/\ \  / __`\/\`'__\/'_` \   \ \ \L_L   /'__`\/' _ `\  /'__`\/\`'__\/'__`\ \ \ \/  / __`\/\`'__\_
  \ \ \/\ \L\.\_/\__, `\/\__, `\ \ \_/ \_/ \/\ \L\ \ \ \//\ \L\ \   \ \ \/, \/\  __//\ \/\ \/\  __/\ \ \//\ \L\.\_\ \ \_/\ \L\ \ \ \/ 
   \ \_\ \__/.\_\/\____/\/\____/\ \___x___/'\ \____/\ \_\\ \___,_\   \ \____/\ \____\ \_\ \_\ \____\\ \_\\ \__/.\_\\ \__\ \____/\ \_\ 
    \/_/\/__/\/_/\/___/  \/___/  \/__//__/   \/___/  \/_/ \/__,_ /    \/___/  \/____/\/_/\/_/\/____/ \/_/ \/__/\/_/ \/__/\/___/  \/_/                                                                                                    

"""

def random_password_generator(letters, numbers, symbols, nr_letters,nr_symbols, nr_numbers):
 
  password = ""; #my empty password variable that i'd be working with later

  loop_time = nr_letters+nr_numbers+nr_symbols; #calculating the final loop time for all the character to be produced.

  for _ in range(1, loop_time +1): #looping loop_time amount of times.
      
      valid_letter = letters[r.randint(1,len(letters) -1)]; #getting a random letter
      valid_number = numbers[r.randint(1,len(numbers) -1)]; #getting a random number
      valid_symbol = symbols[r.randint(1,len(symbols) -1)]; # getting a random symbol

      options = {1: valid_letter, 2: valid_number, 3: valid_symbol}; #creating a dictionary of all options.

      choice = r.randint(1,len(options)); #getting a random choice from the dictionary
      
      password += options[choice]; #appending the choice to the password variable
  print(f" 🔐: \"{password}\" ");#self explanatory
  pass;


def main():
    print(logo);
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    random_password_generator(letters, numbers, symbols, nr_letters, nr_symbols, nr_numbers);
    pass;

main();