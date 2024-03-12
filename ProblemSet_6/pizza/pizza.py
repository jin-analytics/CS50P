from tabulate import tabulate
import sys
import csv

with open(sys.argv[1]) as file:
    for line in file:
        #splits by comma and remoceves with rstrip garbage like "/n"
        row = line.rstrip().split(',')
        print(row)
        #print(tabulate(row))
