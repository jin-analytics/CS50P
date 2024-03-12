from tabulate import tabulate
import sys
import csv

with open(sys.argv[1]) as file:
    for line in file:
        #splits by comma and remoceves with rstrip garbage like "/n"
        item, small_price, large_price = line.rstrip().split(',')
        print(item, small_price, large_price)
        #print(tabulate(row))
