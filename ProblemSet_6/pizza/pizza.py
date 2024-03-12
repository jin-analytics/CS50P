from tabulate import tabulate
import sys
import csv

order = []
table = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)

    for row in reader:
        order.append(f"{row[0]},{row[1]},{row[2]}")
    #print([order[0]],[order[1]])

    for entrees in order:
        table.append([entrees])
    print(table)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
