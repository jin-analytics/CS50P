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
#     $         matches the end of the string or just
#               ...before the newline at the end of the string
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



email = input('whats your mail? \n').strip()

# ^     matches at the start of the string
# /w    accepts 'a,b,...,z | A,B,...,Z | 0,1,...,9 | _'
# +     atleast one character of /w or more
# @     matches the previous string until @ arrives
# /w    accepts 'a,b,...,z | A,B,...,Z | 0,1,...,9 | _' after the @
# +     atleast one character of /w or more until the .com
# $     matches the end of the string

if re.search(r"^\w+[.]$@\w+\.com$", email, re.IGNORECASE):
    print('valid')
else:
    print('invalid')














