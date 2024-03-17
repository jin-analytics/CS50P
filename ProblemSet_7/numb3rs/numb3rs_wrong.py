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
         return False
         #sys.exit()
    # each number in '#' must be [0:255]
    if number_under_256(ip) != True:
         return False

def number_format_in_dot_decimal(ip):
    # ^         takes the start of the string, first character
    # (\d+)     just accepts a group of number from 0 to 9 and has to be atleast one number
    # \.        the previous number string has to end with: "."
    # (\d{1,3}) takes any number string from 1 to 3 entrees in it
    # $         matches the end of the string... so for input "1.2.3.4"
    #           ... ip = ['1','2.3.4']

    #if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip): #correct version
    if re.search(r"^(\d{1,3})\.([a-zA-Z0-9.]*)$", ip): #version which just checks first byte and accepts letters,number,dots
        return True
    else:
        #print('no match')
        return False

def number_under_256(ip):
    ip = re.findall(r"^(\d{1,3})\.([a-zA-Z0-9.]*)$", ip)
    # with re.findall ip becomes a tuple (#,#,#,#). Example for access entree #3: ip[0][2]
    for _ in range(4):
        if int(ip[0][int(0)]) > 255:    #ip[0][int(_)] iterates through the 4 numbers of tuple and
            return False                #...converts the str numbers to int numbers for comparison




if __name__ == "__main__":
    main()


