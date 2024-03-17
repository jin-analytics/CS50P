import re
import sys

#____pattern_____________________________________________________________
#     .         any character except a newline
#     *         0 or more repetitions
#     +         1 or more repetitions
#     ?         0 or 1 repetition
#     {m}       m repetitions
#     {m,n}     m-n repetitions
#     ^         matches the start of the string
#     $         matches the end of the string
#     []        set of characters
#     [^]       complementing the set (opposite)
# [a-zA-Z0-9_ ] include a,b,...,z/A,B,...,Z/0,1,...,9,_,'space'
#     \d        decimal digit
#     \D        not a decimal digit
#     \s        whitespace character
#     \S        not a whitespace character
#     \w        word character...as well as numbers and the _
#     \W        not a  word character...as well as numbers and the _
#     A|B       either A or B
#     (...)     a group
#     (?:...)   non capturing version


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


# validate() expects a str as input and return True or False
def validate(ip):
    # IPv4 must have this format '#.#.#.#' and '#' just being numbers
    if number_format_in_dot_decimal(ip) != True:
         sys.exit()

#    # each number in '#' must be [0:255]
#    if number_between_0_and_255(ip) != True:
#         sys.exit()

    return True


def number_format_in_dot_decimal(ip):
    if matches := re.search(r"", ip):
        byte1 = matches.group(1)
        print(f"{ip}")
        print(f"{byte1}")



















def number_between_0_and_255(ip):
        #ip = re.split(r'^(\d+).(\d+).(\d+).(\d+)$',ip)
        #modification for first byte check:
    if re.search(r'^(\d+)',ip):
        ip = ''.join(ip).split('.',1)
        print(ip)
        #for numbers in ip:
        for numbers in ip:
             #print(numbers)
             if int(numbers) > 255: #negative numbers gets detected through format check
                  return print(False)
        return True


if __name__ == "__main__":
    main()


