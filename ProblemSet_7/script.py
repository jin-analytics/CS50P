### Script for Lecture 7

#re.search(pattern,string,flags=0)
import re

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

#____flags_______________________________________________________________
#    re.IGNORECASE      ignore uppercase, lowercase,...
#    re.MULTILINE
#    re.DOTALL


# Example No.1
def example1():
    email = input('whats your mail? \n').strip()

    # ^     matches at the start of the string
    # /w    accepts 'a,b,...,z | A,B,...,Z | 0,1,...,9 | _'
    # +     atleast one character of /w or more
    # @     matches the previous string until @ arrives
    # /w    accepts 'a,b,...,z | A,B,...,Z | 0,1,...,9 | _' after the @
    # +     atleast one character of /w or more until the .com
    # $     matches the end of the string

    if re.search(r"^\w+.?\w*@\w+.?\w*\.com$", email, re.IGNORECASE):
        print('valid')
    else:
        print('invalid')

# Example No. 2
def example2():
    name = input("whats your name? ").strip()
    if matches := re.search(r"^(.+), (.+)$", name):
        last = matches.group(1)
        first = matches.group(2)
        name = f"{first} {last}"
        #name = matches.group(2) + " " matches.group(1 )
    print(f"hello, {name}")

# Example No.3
def example3():
    












