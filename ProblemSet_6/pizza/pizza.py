from tabulate import tabulate
import sys
import csv



def main():
    order = []
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")

        with open(sys.argv[1]) as file:
            reader = csv.reader(file)

            for row in reader:
                order.append(row)

            print(tabulate(order, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit('File does not exist')
    except IndexError:
        sys.exit('File does not exist')

if __name__ == "__main__":
    main()
