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
    elif number_under_256(ip) != True:
        return False
    else:
        return True


def number_format_in_dot_decimal(ip):
    if re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        return True
    else:
        return False


def number_under_256(ip):
    ip = re.findall(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    # with re.findall, ip becomes a tuple (#,#,#,#). Example for access entree #3: ip[0][2]
    for _ in range(4):
        if int(ip[0][int(_)]) > 255:    #ip[0][int(_)] iterates through the 4 numbers of tuple and
            return False                #...converts the str numbers to int numbers for comparison
    return True


if __name__ == "__main__":
    main()


