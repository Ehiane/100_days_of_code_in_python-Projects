
#! here are some list comprehension tactics
file1_nums,file2_nums = [],[]; #initialise both lists.

with open("file1.txt","r") as f1: #open the file
    contents = f1.readlines(); #stored all the contents of the file in a list
    file1_nums = [int(x) for x in contents if x!= "\n"]; #used list comprehension to convert 
    #all the non "\n" elements to integers and assigned that to list 1;

with open("file2.txt","r") as f2:
    # similar to lines 3-6
    contents = f2.readlines();
    file2_nums = [int(x) for x in contents if x!= '\n'];

#* used list comprhension to find common values in both lists.
result = [x for x in file1_nums if x in file1_nums and x in file2_nums];



# Write your code above 👆

print(result)


