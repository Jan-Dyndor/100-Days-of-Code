# with open("weather_data.csv", mode="r") as data_f:
#     data = data_f.readlines()
# print(data)


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data) # Created an object
#     temperatures = []
#     for row in data:
#         if row[1] =="temp":
#             continue
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)
#


import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# #  Series = like a list
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in ROWS
# monday = data[data["day"] == "Monday"]
# print(monday)
#
# # Max temp
# max_temp = data[data["temp"] == data["temp"].max()]
# #! When a particular column is equal to particular value - we get a row
# print(max_temp)

# monday = data[data.day == "Monday"]
# monday_temp_F = monday["temp"] * 1.8 + 32
# print(monday_temp_F)

# Create DataFrame from scratch
# data_dict = {
#     "students": ["Anna", "Jakub", "Jan"],
#     "scores": [20, 33, 19]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirell_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = squirell_data["Primary Fur Color"].value_counts()["Black"]
red = squirell_data["Primary Fur Color"].value_counts()["Cinnamon"]
grey = squirell_data["Primary Fur Color"].value_counts()["Gray"]

squirell_collors_count = {
    "Fur Color": ["black", "red", "grey"],
    "Count": [black, red, grey]
}

squirell_collors_count_df = pandas.DataFrame(squirell_collors_count)
print(squirell_collors_count_df)
squirell_collors_count_df.to_csv("squirrel_collors_counts.csv")