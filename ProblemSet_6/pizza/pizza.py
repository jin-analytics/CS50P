from tabulate import tabulate
import sys
import csv

with open(sys.argv[1]) as file:
    for line in file:
        print(line.rstrip().split(','))
