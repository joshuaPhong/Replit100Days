# import the csv library
import csv
# declare variables
cost = 0
quantity = 0
takings = 0
# read the file in
with open("Day_54_Totals.csv") as day:
    day_54 = csv.DictReader(day)
#     loop through the rows
    for row in day_54:
        cost = float(row["Cost"])
        quantity = float(row["Quantity"])
        takings += (cost * quantity)
    print(f"The days takings are {takings}")




