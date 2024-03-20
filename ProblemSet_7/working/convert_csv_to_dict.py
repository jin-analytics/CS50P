import json
import csv

# creates a dictionary
reader = csv.reader(open('hour_format.csv', 'r'))
    d = {}
    next(reader)
    for row in reader:
        key, val = row
        d[key] = val

# prints the dictionary to a text file
    with open('hour_format.txt', 'w') as file:
        file.write(json.dumps(d))
