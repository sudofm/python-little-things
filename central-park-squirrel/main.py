# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"].tolist()
# avg_temp = sum(temperatures)/len(temperatures)
# print(avg_temp)
# avg = data["temp"].mean()
# print(avg)
#
# print(data["temp"].max())
# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp[0] * 9/5 + 32
# print(monday_temp_F)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250505.csv")
#data["Primary Fur Color"].value_counts().to_csv("squirrel_count.csv")
grey_squirrels_count =  len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count2.csv")