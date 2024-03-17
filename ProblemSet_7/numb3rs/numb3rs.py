import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


# validate() expects a str as input and return True or False
def validate(ip):
    # IPv4 must have this format '#.#.#.#' and '#' just being numbers
    if number_format_in_dot_decimal(ip) != True:
        return False
    # each number in '#' must be [0:255]
    elif number_between_0_and_255(ip) != True:
        return False
    else:
        return True


def number_format_in_dot_decimal(ip):
    if re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        ip = ''.join(ip).split('.')
        if len(ip) == 4:
            return True
    else:
        return print(False)


def number_between_0_and_255(ip):
    if re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$',ip):
        ip = ''.join(ip).split('.')
        for numbers in ip:
             if int(numbers) > 255: #negative numbers gets detected through format check
                  return print(False)
        return True


if __name__ == "__main__":
    main()


