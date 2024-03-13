# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

with open("before.csv", "r") as csvfile:
    for line in csvfile:
        line = line.rstrip().split(",")
    print(csvfile)
