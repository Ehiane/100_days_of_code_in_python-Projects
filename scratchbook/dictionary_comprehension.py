
## SYNTAX: new_dict = {<new_key>: <new_value> for <key> in <iterable> };
## SYNTAX: new_dict = {<new_key>: <new_value> for (key,value) in existing iterable.items() + <condition>};

import random as r
import pandas

names = ["Ehis","Kelvin","Timothy","Josiah","Tyrone"]
students_scores = {student: r.randint(1,100) for student in names};
# print(students_scores); #{'Ehis': 91, 'Kelvin': 22, 'Timothy': 96, 'Josiah': 30, 'Tyrone': 31}


# creates a dictionary of all students who scored more than 50%
passed_students = {student:value for (student,value) in students_scores.items() if value> 50 }
# print(passed_students);




weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

def convert(c):
    return((c *9/5) +32);

weather_f = {day:convert(temp) for (day, temp) in weather_c.items()}

# Write your code 👇 below:

# print(weather_f)




student_dict = {
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}
student_data_frame = pandas.DataFrame(student_dict);
# print(student_data_frame)

# loop through
# for(key,value) in student_data_frame.items():
#     print(value);

# inbuilt loop 
# for(index, row)in student_data_frame.iterrows():
#     # print(row,"\n");
#     # print(row.student,"\n"); #prints all the students
#     if row.student == "Angela":
#         print(row.score); #will print out angela's score.


# Im trying to map a number to it's status(prime or no prime)
numbers = [x for x in range(1,101)];

def status(number):
    """
    Precondition: number argument > 1;
    """
    if number % 2 == 0:
        return "Even";
    else:
        return "Odd"


number_status_dict = {number:status(number) for number in numbers};
print(number_status_dict);
