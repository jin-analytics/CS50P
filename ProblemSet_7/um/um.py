import re
import sys


def main():
    print(count(input("Text: ")))
# test um, if um gets detected

def count(s):
    counter = []

    s = re.split(r'\W+', s) # this splits also the comma... "um," -> \W+ is better

    for entrees in s:
        if entrees == "um":
            counter.append(1)

    return len(counter)



if __name__ == "__main__":
    main()
