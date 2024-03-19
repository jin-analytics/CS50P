# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

# implement a function called parse():
# - that expects a str of HTML as input,
# - extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
# - and returns its shorter,
# - shareable youtu.be equivalent as a str
#
# Possible inputs:
# input: http://youtube.com/embed/xvFZjo5PgG0
# input: https://youtube.com/embed/xvFZjo5PgG0
# input: https://www.youtube.com/embed/xvFZjo5PgG0
# Assume that the value of src will be surrounded by double quotes
# If the input does not contain any such URL at all, return None


import re
import sys


def main():

    print(parse(input("HTML: ")))

def parse(s):

    ####s = re.findall(r'^(\"[a-zA-Z0-9:/.]+\")+$', s) #THIS CATCHES A YOUTUBE STRING
    ###s = re.findall(r'^<iframe(.+)src=\"([a-zA-Z0-9:/.]+)\"(.+)$', s, re.MULTILINE) # THIS CATCHES THE REQUIRED STRING
    ###print(s[0][1])
    ###return True
    s = re.search(r'^<iframe(.+)src=\"([a-zA-Z0-9:/.]+)\"(.+)$', s, re.MULTILINE)
    print(s)


#<iframe width="560
...


if __name__ == "__main__":
    main()

