import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# validate() expects a str as input and return True or False
def validate(ip):
    # IPv4 must have this format '#.#.#.#'
    if number_format_in_dot_decimal(ip) != True:
         sys.exit()
    # each number in '#' must be [0:255]
    if number_between_0_and_255(ip) != True:
         sys.exit()

    return True


def number_format_in_dot_decimal(ip):
    #test if i can split 3 dots
    if re.search(r'^(\d+).(\d+).(\d+).(\d+)$',ip):
        return True
    else:
        return print(False)


def number_between_0_and_255(ip):
        ip = re.split(r'^(\d+).(\d+).(\d+).(\d+)$',ip)
        ip = ' '.join(ip).split()
        for numbers in ip:
             if int(numbers) > 255: #negative numbers gets detected through format check
                  return print(False)
        return True


if __name__ == "__main__":
    main()


