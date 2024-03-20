import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    #       9:AM to 5:00PM
    s = re.findall(r'^$', s) # THIS CATCHES THE REQUIRED STRING





if __name__ == "__main__":
    main()
