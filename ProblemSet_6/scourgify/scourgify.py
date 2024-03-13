# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

with open("before.csv", "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for line in csvfile:
        print(line)

    with open("test.csv", "w") as newfile:
        fieldnames = ["name", "house"]
        csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        #csv_writer.writeheader()

#        for line in newfile:
#            csv_writer.writerow(fieldnames)
#            print(line)
