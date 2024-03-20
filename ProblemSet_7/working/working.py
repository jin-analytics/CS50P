import re
import sys
import csv
import json

# create csv file which has the 12-Hour and 24-Hour implemented
# make a dict out of it

table = {"12:00 AM": "00:00",
         "1:00 AM": "01:00",
         "2:00 AM": "02:00",
         "3:00 AM": "03:00",
         "4:00 AM": "04:00",
         "5:00 AM": "05:00",
         "6:00 AM": "06:00",
         "7:00 AM": "07:00",
         "8:00 AM": "08:00",
         "9:00 AM": "09:00",
         "10:00 AM": "10:00",
         "11:00 AM": "11:00",
         "12:00 PM": "12:00",
         "1:00 PM": "13:00",
         "2:00 PM": "14:00",
         "3:00 PM": "15:00",
         "4:00 PM": "16:00",
         "5:00 PM": "17:00",
         "6:00 PM": "18:00",
         "7:00 PM": "19:00",
         "8:00 PM": "20:00",
         "9:00 PM": "21:00",
         "10:00 PM": "22:00",
         "11:00 PM": "23:00"}


def main():
    print(convert(input("Hours: ")))



def convert(s):
    for key12,value24 in table.items():
        if s == key12:
            print(f'{key12} is equal to {value24}')
    #       9:AM to 5:00PM
    s = re.findall(r'^$', s) # THIS CATCHES THE REQUIRED STRING





if __name__ == "__main__":
    main()
