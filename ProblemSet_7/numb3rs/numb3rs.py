import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# validate() expects a str as input and return True or False
def validate(ip):

    # IPv4 must have this format '#.#.#.#'
    print('format check', number_format_in_dot_decimal(ip))

    # each number in '#' must be [0:255]
    print('number check',number_between_0_and_255(ip))

    sys.exit()


def number_format_in_dot_decimal(ip):
    #test if i can split 3 dots
    if re.search(r'^(\d+).(\d+).(\d+).(\d+)$',ip):
        return True
    else:
        sys.exit()


def number_between_0_and_255(ip):
    #if matches := re.search(r'^(\d+).(\d+).(\d+).(\d+)$',ip):
        #num1 = int(matches.group(1))
        ip = ip.strip()
        if matches := re.findall(r'^(\d+).(\d+).(\d+).(\d+)$',ip):
            print(matches[1])




        #print(f'{matches.group(1)},{matches.group(2)},{matches.group(3)},{matches.group(4)}')


if __name__ == "__main__":
    main()


