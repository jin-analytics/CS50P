import re
import sys


def main():
    print(count(input("Text: ")))
# test um, if um gets detected

def count(s):
    s = re.split(r'\w+', s)
    print(s)

    if matches := re.search(r'^([um]*)$', s):
        print(f'...', matches.group())


if __name__ == "__main__":
    main()
