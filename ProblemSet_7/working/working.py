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

#ziel:
# HH:MM AM -> MM Extrahieren
# HH:MM AM-> Auf HH:00 bringen zum matchen


def main():
    print(convert(input("Hours: ")))

#       9:00 AM to 5:00 PM
#    10:30 PM to 8:50 AM

def convert(s):

    # This catches hh:mm AM/PM and gives each to a variable
    s = re.findall(r'^(\d+\:*\d*\s+[AM]*[PM]*) to+ (\d+\:*\d*\s+[AM]*[PM]*)$', s) # THIS CATCHES THE REQUIRED STRING
    hour,minute,daytime = re.split("[: ]",s[0][0])
    print(hour)
    print(minute)
    print(daytime)

    # Adjust hh:mm AM/PM to hh:00 AM/PM, so that the pair gets found in the dictionary "table"
    #v = f"{hour}:00 {daytime}"
    #print(v)
    for key,value in table.items():
        if f"{hour}:00 {daytime}" == key:
           print(f'{key} is equal to {value}')
           break




    #print("{:02}".format(n))
    #print(f"{n:02}")


    #for key,value in table.items():
    #    if s[0][0] == key:
    #       print(f'{key[0]} is equal to {value[0:2]}')




if __name__ == "__main__":
    main()
