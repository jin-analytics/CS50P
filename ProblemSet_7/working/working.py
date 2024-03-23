import re
import sys

# Dictionary which has the hours of 12h format assigned to hours of 24h format
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

# Input example:    10:30 PM to 8:50 AM

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        # This catches hh:mm AM/PM and gives each to a variable
        s = re.findall(r'^(\d+\:*\d*\s+[AM]*[PM]*) to+ (\d+\:*\d*\s+[AM]*[PM]*)$', s) # THIS CATCHES THE REQUIRED STRING
        # If re.findall() didn't foound something due to incorrect input

        if len(s) == 0:
            raise ValueError

        # If the input includes minutes... for example: 10:30 AM
        if len(re.split("[: ]",s[0][0])) == 3:
            hour0,minute_correct0,daytime0 = re.split("[: ]",s[0][0])
            if int(minute_correct0) > 59:                    # If minute input is not legit, system exits
                raise ValueError
            for key,value in table.items():
                if f"{hour0}:00 {daytime0}" == key:          # If correct input format, the hour will be found in the dictionary
                    hour0, minute0= re.split("[:]", value)   # split the assiged value at ":" to get the minute and hour from the 24h format
                    time0 = f"{hour0}:{minute_correct0}"     # Adjust the new string with 24h format
                    break

        if len(re.split("[: ]",s[0][1])) == 3:
            hour1,minute_correct1,daytime1 = re.split("[: ]",s[0][1])
            if int(minute_correct1) > 59:
                raise ValueError
            for key,value in table.items():
                if f"{hour1}:00 {daytime1}" == key:
                    hour1, minute1= re.split("[:]", value)
                    time1 = f"{hour1}:{minute_correct1}"
                    break


        # If the input don't include minutes... for example: 10 AM
        if len(re.split("[: ]",s[0][0])) == 2:
            hour0,daytime0 = re.split("[: ]",s[0][0])
            if int(minute_correct0) > 59:
                raise ValueError
            for key,value in table.items():
                if f"{hour0}:00 {daytime0}" == key:
                    time0 = f"{key}"
                    break

        if len(re.split("[: ]",s[0][1])) == 2:
            hour1,daytime1 = re.split("[: ]",s[0][1])
            if int(minute_correct0) > 59:
                raise ValueError
            for key,value in table.items():
                if f"{hour1}:00 {daytime1}" == key:
                    time1 = f"{key}"
                    break

        return f"{time0} to {time1}"    # returns the converted time from 12h to 24h format

    except EOFError:
        sys.exit()
    except ValueError:
        return ValueError


if __name__ == "__main__":
    main()
