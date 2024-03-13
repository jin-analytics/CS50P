# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

students = []

with open("before.csv") as csvfile:

### Option 1 - Read out every single line, split it by comma and append to an empty list
#    for line in csvfile:
#        row = line.rstrip().split(",")
#        students.append(row)
#    print(students)

### Option 2 - Use the csv.reader() which splits automaticly by comma and append the single lines to an empty list
#    reader = csv.reader(csvfile)
#    for line in reader:
#        students.append(line)
#    print(students)

### Option 3 - Read out every single line, split it by comma and append to an empty dictionary
    next(csvfile)
    for line in csvfile:
        line = line.rstrip().split(",")
        name, house = csvfile(line)
        #students.append(line)
        student = {"name":name, "house": house}
        #for row in students:

    print(students)
