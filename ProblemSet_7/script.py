### Script for Lecture 7

#re.search(pattern,string,flags=0)
import re

#____pattern
#     .         any character except a newline
#     *         0 or more repetitions
#     +         1 or more repetitions
#     ?         0 or more repetitions
#     {m}       m repetitions
#     {m,n}     m-n repetitions
#     ^         matches the start of the string
#     $         matches the end of the stringor just
#               ...before the newline at the end of the string
#     []        set of characters
#     [^]       complementing the set (opposite)
# [a-zA-Z0-9_]  exclude a,b,...,z/A,B,...,Z/0,1,...,9 and _
#     \d        decimal digit
#     \D        not a decimal
#     \s        not a word character
#     \S        not a word character
#     \w        not a word character
#     \w        not a word character


email = input('whats your mail? \n').strip()

if re.search(r"^.+[^@]@.+[^@]\.com$", email):
    print('valid')
else:
    print('invalid')














