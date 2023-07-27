
## Special Python Function arguments
# * Default values -- very similar to c/c++
# * "*args":
"""
!WITH THIS, YOU CAN PASS IN MULTIPLE AMOUNT OF ARGUMENTS, AND WHATEVER HAPPENS WILL BE PERFORMED
!WITH A LOOP.

def add(*args):
    for n in args:
        #do whatever!
"""

def add(*args):
    result = 0;
    for n in args:
        result += n;
    return result; 


total = add(5,10,15,20,25,30,45,50,55,60); #doesn't work with lists.
# print(total);


# * '**kwargs':
def calculate(n, **kwargs):
    print(kwargs, type(kwargs)); #Data Structure: dictionary.

    n += kwargs["add"];
    n *= kwargs["multiply"];
    print(n);

# calculate(n = 2 ,add = 3, multiply=5);


# trying to understand how to use **kwargs:

class Car:
    def __init__(self, **kw):
        """
        !USING THE '.get' FOR '**kwargs' WOULD 
        !ALLOW YOU TO USE KWARGS OPTIONALLY
        """
        self.make = kw.get("make");
        self.model = kw.get("model");
        self.color = kw.get("color");
        self.seats = kw.get("seats");


my_car = Car(make = "Nissan", model= "GT-R");
print(my_car.model);
print(my_car.make);