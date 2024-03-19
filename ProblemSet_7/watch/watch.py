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
    try:
        ####s = re.findall(r'^(\"[a-zA-Z0-9:/.]+\")+$', s) #THIS CATCHES A YOUTUBE STRING
        s = re.findall(r'^<iframe(.+)src=\"([a-zA-Z0-9:/.]+)\"(.+)$', s, re.MULTILINE) # THIS CATCHES THE REQUIRED STRING
        #print(s[0][1])
        # CHECK FOR HTTP, SO THAT IT WILL BE REPLACED WITH HTTPS
        if re.findall(r'https([a-zA-Z0-9:/.]+)$', s[0][1]):
            short = re.sub('be.com/embed','.be', s[0][1])
            short = re.sub('https://www.','https://', short)
            if short != s[0][1]:
                return short

        short = re.sub('http://www.','https://', s[0][1])
        short = re.sub('be.com/embed','.be', short)
        if short != s[0][1]:
                return short
        else:
            return None

    except IndexError:
        return None


if __name__ == "__main__":
    main()

