from tabulate import tabulate
import sys
import csv

with open(sys.argv[1], newline='') as csvfile:
    for entrees in csvfile:
        #spamreader = csv.reader(csvfile)
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
