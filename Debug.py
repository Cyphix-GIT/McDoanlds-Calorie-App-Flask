import csv

category = "Breakfast"
food_item, calories = [], []
with open("menu.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    for row in data:
        if row[0] == category:
            food_item.append(row[1])
            calories.append(row[3])
print(food_item)
print(calories)
