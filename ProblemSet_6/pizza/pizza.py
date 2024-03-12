from tabulate import tabulate
import sys
import csv

order = []
table = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)

    for row in reader:
        order.append(row)

    print(tabulate(order, headers="firstrow", tablefmt="grid"))
