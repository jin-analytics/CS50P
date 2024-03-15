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



email = input('whats your mail? \n').strip()

if re.search(".+@.+\.com", email):
    print('valid')
else:
    print('invalid')
