# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

storage = []

with open("before.csv", "r") as csvfile:
    for line in csvfile:
        row = line.rstrip().split(",")
        storage.append(row)

    print(storage[2])
