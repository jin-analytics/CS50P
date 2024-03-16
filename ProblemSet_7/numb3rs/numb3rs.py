import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# validate() expects a str as input and return True or False
def validate(ip):

    # IPv4 must have this format '#.#.#.#'
    number_format_in_dot_decimal(ip)

    # each number in '#' must be [0:255]
    number_between_0_and_255(ip)

    return True


def number_format_in_dot_decimal(ip):



def number_between_0_and_255(ip):
    ...


if __name__ == "__main__":
    main()


