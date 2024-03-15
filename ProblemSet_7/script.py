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
#



email = input('whats your mail? \n').strip()

if re.search(r".+@.+\.com$", email):
    print('valid')
else:
    print('invalid')
