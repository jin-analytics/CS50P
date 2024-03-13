# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

with open("before.csv", "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for line in csvfile:
        print(line)

