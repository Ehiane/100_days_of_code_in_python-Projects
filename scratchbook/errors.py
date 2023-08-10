
## Understaning the types of errors in python:
# Key Error
# Index error
#  Type error
# File not found
# syntax error
# ...


## Catching Exceptions
#@ syntax:
"""
try: {smth that might cause an exception}
except: {do this if there was an exception}
else: {do this if there were no exceptions}
finally: {do this no matter what happens}
"""

#@ Regular example
"""
try:
    file = open("afile.txt");
except:
    file = open("afile.txt","w");
"""

#@ specifiying the type of exception.
# if you're not specific with your "except" error datatype,
# then if there is an error in one of the "try" blocks, it'' default to the "except" class

"""
try:
    file = open("afile.txt");
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except FileNotFoundError:
    file=open("afile.txt","w");
    file.write("smth");
except KeyError:
    print("That key does not exist.")
"""
    
#@ getting hold of the key error as string.
"""
try:
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except KeyError as error_msg:
    print(f"The key {error_msg}, does not exist."); #the key "ghg" does not exist
"""

#@ else case(when no error has been met.)
"""
try:
    file = open("afile.txt");
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except FileNotFoundError:
    file=open("afile.txt","w");
    file.write("smth");
else:
    # as long both previous conditions are not met, this will run.
    content = file.read();
    print(content);
"""

#@ The finally case (runs no matter what.)
"""
try:
    file = open("afile.txt");
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except FileNotFoundError:
    file=open("afile.txt","w");
    file.write("smth");
else:
    content = file.read();
    print(content);
finally:
     # this will run no matter what.
    file.close();
    print("file was closed.")
"""


#@ The "raise" keyword (custom exception)
"""
try:
    file = open("afile.txt");
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except FileNotFoundError:
    file=open("afile.txt","w");
    file.write("smth");
else:
    content = file.read();
    print(content);
finally:
    # this will run no matter what.
    # file.close();
    # print("file was closed.")
    raise TypeError("This is an error that i made up"); #will raiset his error with this specific mssg.

"""


height = float(input("Height: "));
weight = float(input("Weight: "));

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2;
print(bmi);