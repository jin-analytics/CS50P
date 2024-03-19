import re
import sys


def main():

    print(parse(input("HTML: ")))

def parse(s):
    try:
        ####s = re.findall(r'^(\"[a-zA-Z0-9:/.]+\")+$', s) #THIS CATCHES A YOUTUBE STRING
        s = re.findall(r'^<iframe(.+)src=\"([a-zA-Z0-9:/.]+)\"(.+)$', s, re.MULTILINE) # THIS CATCHES THE REQUIRED STRING

        if re.findall(r'https([a-zA-Z0-9:/.]+)$', s[0][1]):
            short = re.sub('be.com/embed','.be', s[0][1])
            short = re.sub('https://','https://', short)
            short = re.sub('www.','', short)
            if short != s[0][1]:
                return short

        # HTTP WILL BE REPLACED WITH HTTPS
        short = re.sub('be.com/embed','.be', s[0][1])
        short = re.sub('http://','https://', short)
        short = re.sub('www.','', short)
        if short != s[0][1]:
                return short
        else:
            return None

    except IndexError:
        return None


if __name__ == "__main__":
    main()

