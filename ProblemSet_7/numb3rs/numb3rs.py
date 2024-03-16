import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# validate() expects a str as input and return True or False
def validate(ip):

    # IPv4 must have this format '#.#.#.#'
    number_format_in_dot_decimal()

    # each number in '#' must be [0:255]
    number_between_0_and_255()




def number_format_in_dot_decimal():
    ...


def number_between_0_and_255():
    ...


if __name__ == "__main__":
    main()


