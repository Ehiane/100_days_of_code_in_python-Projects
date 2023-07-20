import pandas
import time


FILE_NAME = (
    "analysingSquirrelData/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)


QUERRY = "Primary Fur Color"


# $ QUESTION:
"""
find how many gray, cinnamon and black squirrels they are individually 
and build a new data frame from that
"""

# your own dataset should be like this:
"""
, Fur , count
0, ... , ...
1, ... , ...
2, ... , ...
"""

start = time.time()
# initialise the existing dataset to a dataframe.
database = pandas.read_csv(FILE_NAME)

# access to the column with all the fur colors.
fur_color_column = database[QUERRY]


fur_colors = ["Gray", "Cinnamon", "Black"]


## This works:
# def get_num_colors(fur_color, Dataset):
#     count = 0
#     for row in Dataset:
#         if row == fur_color:
#             count += 1
#     return count


# cinnamon_count = get_num_colors(fur_colors[1], fur_color_column)
# gray_count = get_num_colors(fur_colors[0], fur_color_column)
# black_count = get_num_colors(fur_colors[2], fur_color_column)

## Here is a better way [apparently it took longer 🤣]:
gray_count = len(database[database[QUERRY] == fur_colors[0]]);
cinnamon_count = len(database[database[QUERRY] == fur_colors[1]]);
black_count = len(database[database[QUERRY] == fur_colors[2]]);

counts = [gray_count, cinnamon_count, black_count]
# make a data structure:
custom_data = {
    "Fur Color": fur_colors,
    "Count": counts,
}

# making a new data frame.
new_dataset = pandas.DataFrame(custom_data)

new_dataset.to_csv("analysingSquirrelData/personal_fur_count.csv")
end = time.time()

print(new_dataset)
print(f"time spent: {end - start}")
