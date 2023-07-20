import pandas;
import time;


def c_to_f(c):
    conversion = (c * 9/5) + 32;
    return conversion;


def main():
    # print(type(data)); #type dataFrame: a dataframe is like the whole table.
    data = pandas.read_csv("weather_data.csv") ## A DataFrame

    # # you can use the title of a column to search for the values of that column.
    # temp_data_series = data["temp"]; ## A series(temp) | allias:  data.temp will work as well

    # # you can access a column in a series by dot notation. pandas takes the names of the columns and adds them as attributes to the specific dataFrame you are working with.
    # # print(type(data["temp"])); #type series: it's like a column or row. a part of a dataframe.

    # data_dict = data.to_dict()
    # # print(data_dict);

    # # Visualisation of data_dict
    # """
    # {
    #     "day": {
    #         0: "Monday",
    #         1: "Tuesday",
    #         2: "Wednesday",
    #         3: "Thursday",
    #         4: "Friday",
    #         5: "Saturday",
    #         6: "Sunday",
    #     },
    #     "temp": {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
    #     "condition": {
    #         0: "Sunny",
    #         1: "Rain",
    #         2: "Rain",
    #         3: "Cloudy",
    #         4: "Sunny",
    #         5: "Sunny",
    #         6: "Sunny",
    #     },
    # }
    # """
    

    # data_list = data["temp"].to_list();
    # # print(data_list);

    # # Visualisation of data_list
    # """
    # [12, 14, 15, 14, 21, 22, 24]
    # """
    

    
    # # finding mean:
    # temp_mean =  temp_data_series.mean();
    # # print(temp_mean);
    
    # # calculating time for it to find the max value.
    # start_time = time.time();
    # max_temp = temp_data_series.max()
    # end_time = time.time();

    # operation_duration = end_time - start_time;

    # print(max_temp, f"it took {operation_duration} s to get this result.");

    ##To find a row in the dataFrame
    # this will print out everything in that row where monday is present.
    # print(data[data.day == "Monday"]);

    """
    RESULT: 

       day      temp    condition
    0  Monday    12     Sunny
    """

    #$ QUESTION:  print out the row of data with the highest temperature of the week.
    """
    RESULT:
        day    temp     condition
    6  Sunday    24     Sunny
    """
    # print(data[data.temp == data["temp"].max()]);


    #$ QUESTION:  convert the temp in monday to farenheit.
    monday = data[data.day == "Monday"]; #row : a pandas dataFrame 
    monday_temp_in_f = c_to_f(monday.temp);
    # print(monday_temp_in_f);
    
    ## how to create a dataframe from scratch
    
    # have viable data:
    Data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores":[76, 56, 65], 
    }

    #call the pandas module and pass it through the class and it becomes a data frame.
    custom_data = pandas.DataFrame(Data_dict);
    """
    Result:

            students  scores
        0      Amy      76
        1    James      56
        2   Angela      65
    """
    ## you can even convert it to a csv now .
    custom_data.to_csv("custom_stats.csv");
    print(custom_data);
    pass;








main()
