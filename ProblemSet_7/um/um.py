import re
import sys


def main():
    print(count(input("Text: ")))
# test um, if um gets detected

def count(s):
    # empty list, which gets filled through the for loop
    counter = []

    s = re.split(r'\W+', s) # \s splits also the comma... "um," -> \W+ is better

    # appends the counter list with 1 for every "um"
    for _ in s:
        if _ == "um":
            counter.append(1)

    # returns the length of counter list
    return len(counter)



if __name__ == "__main__":
    main()
