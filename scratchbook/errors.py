
## Understaning the types of errors in python:
# Key Error
# Index error
#  Type error
# File not found
# syntax error


## Catching Exceptions
# syntax:
"""
try: {smth that might cause an exception}
except: {do this if there was an exception}
else: {do this if there were no exceptions}
finally: {do this no matter what happens}
"""

# try:
#     file = open("afile.txt");
# except:
#     file = open("afile.txt","w");

#@ Specifiying the type of exception.
# if you're not specific with your "except" error datatype,
# then if there is an error in one of the "try" blocks, it'' default to the "except" class

try:
    file = open("afile.txt");
    a_dictionary = {"key":"value"};
    print(a_dictionary["ghg"]);
except FileNotFoundError:
    file=open("afile.txt","w");
    file.write("smth")