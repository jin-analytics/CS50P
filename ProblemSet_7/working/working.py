import re
import sys
import csv

# create csv file which has the 12-Hour and 24-Hour implemented
# make a dict out of it


def main():
    print(convert(input("Hours: ")))



def convert(s):
    with open('hour_format.csv') as file:
            dict = csv.DictReader(file)
            for row in dict:
                for k, v in row.items():
                     print(k,v)


    #       9:AM to 5:00PM
    s = re.findall(r'^$', s) # THIS CATCHES THE REQUIRED STRING





if __name__ == "__main__":
    main()
