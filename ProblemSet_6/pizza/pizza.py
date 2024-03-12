from tabulate import tabulate
import sys
import csv

with open(sys.argv[1]) as csvfile:
    for entrees in csvfile:
        lines = csv.reader(csvfile)
        print(lines)
