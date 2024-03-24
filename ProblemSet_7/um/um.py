import re
import sys


def main():
    print(count(input("Text: ")))
# test um, if um gets detected

def count(s):
    s = re.split(r'\W+', s) # this splits also the comma... "um," -> \W+ is better
    print(s)
    for entrees in s:
        if entrees == "um":
            print(entrees)
        #if matches := re.search(r'^([um]*)$', s):
        #    print(f'...', matches.group())


def counter():
    counter = []
    

if __name__ == "__main__":
    main()
