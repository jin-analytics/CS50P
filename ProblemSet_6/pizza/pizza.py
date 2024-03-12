from tabulate import tabulate
import sys
import csv

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    

    #for line in file:
        ###splits by comma and remoceves with rstrip garbage like "/n"
        #item, s, l = line.rstrip().split(',')
        #print(item, s, l)
        #print(tabulate(item, small_price, large_price))


