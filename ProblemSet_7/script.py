### Script for Lecture 7

#re.search(pattern,string,flags=0)




import re
email = input('whats your mail? \n').strip()

if re.search('@', email):
    print('valid')
else:
    print('invalid')
