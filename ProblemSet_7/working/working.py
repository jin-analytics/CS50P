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

#       9:00 AM to 5:00 PM
#    10:30 PM to 8:50 AM

def convert(s):

    s = re.findall(r'^(\d+\:*\d*\s+[AM]*[PM]*) to+ (\d+\:*\d*\s+[AM]*[PM]*)$', s) # THIS CATCHES THE REQUIRED STRING
    print('Timeframe: ', s[0][0],'to', s[0][1])
    print(f"{n:02}").format()


    #for key,value in table.items():
    #    if s[0][0] == key:
    #       print(f'{key[0]} is equal to {value[0:2]}')




if __name__ == "__main__":
    main()
