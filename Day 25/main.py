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
data = pandas.read_csv("weather_data.csv")
print(data["temp"])


