from tabulate import tabulate
import sys
import csv

order = []
table = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)

    for row in reader:
        order.append(f"{row[0]},{row[1]},{row[2]}")
    print([order[0]],[order[1]])
    #print(tabulate(, headers="firstrow", tablefmt="grid"))
    for entrees in order:
        table.append(entrees)
        print(table)

    #for line in file:
        ###splits by comma and remoceves with rstrip garbage like "/n"
        #item, s, l = line.rstrip().split(',')
        #print(item, s, l)
        #print(tabulate(item, small_price, large_price))
