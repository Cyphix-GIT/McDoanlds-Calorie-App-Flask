from flask import Flask, render_template
import csv

app = Flask(__name__)  # create an instance of the Flask class

categories = []

with open("menu.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    data.__next__()  # skip the header row
    for row in data:
        if row[0] not in categories:  # if the category is not in the list
            categories.append(row[0])  # add it to the list
categories.sort()  # sort the list


@app.route("/", methods=["GET", "POST"])  # route for the home page
def index():
    return render_template(
        "index.html", categories=categories
    )  # render the index.html template


@app.route("/<category>", methods=["GET", "POST"])  # route for the category page
def graph(category):  # pass the category as a parameter
    # print(category)
    food_item, calories = [], []
    with open("menu.csv") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            if row[0] == category:  # if the category matches the parameter
                food_item.append(row[1])  # add the food item to the list
                calories.append(row[3])  # add the calories to the list
    print(food_item)
    print(calories)
    bar_colours = ["blue" for item in food_item]
    if food_item == []:
        return render_template("error.html")
    else:
        return render_template(
            "graph.html",
            category=category,
            food_item=food_item,
            calories=calories,
            bar_colours=bar_colours,
        )


app.run(host="0.0.0.0", port=81)
