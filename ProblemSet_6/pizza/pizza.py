from tabulate import tabulate
import sys
import csv

order = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)

    for row in reader:
        order.append(f"{row[0]},{row[1]},{row[2]}")

    headers = order[0]
    table = order
    print(tabulate(table[1:], headers, tablefmt="grid"))

    #for line in file:
        ###splits by comma and remoceves with rstrip garbage like "/n"
        #item, s, l = line.rstrip().split(',')
        #print(item, s, l)
        #print(tabulate(item, small_price, large_price))
