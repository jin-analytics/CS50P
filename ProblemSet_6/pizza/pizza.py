from tabulate import tabulate
import sys
import csv

order = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row[0])
        order.append(f"{row[0]},{row[1]},{row[2]}")
        order = [[row[0],row[1],row[2]]]
        print(tabulate(order, headers, tablefmt="grid"))

    #for line in file:
        ###splits by comma and remoceves with rstrip garbage like "/n"
        #item, s, l = line.rstrip().split(',')
        #print(item, s, l)
        #print(tabulate(item, small_price, large_price))
