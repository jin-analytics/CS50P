import re
import sys


def main():
    print(count(input("Text: ")))
# test um

def count(s):
    if matches := re.search(r'^\.*([um]*)\.*$', s):
        print(f'...', matches.group(1))


if __name__ == "__main__":
    main()
