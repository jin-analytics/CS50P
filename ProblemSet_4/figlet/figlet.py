import sys
from pyfiglet import Figlet

#Font: italic
# example: f = Figlet(font='slant')
# example: print f.renderText('text to render')

#if len(sys.argv) <2:
#    sys.exit("too few") # sys.exit | exits the program

#for argument in sys.argv[1:]: # Slices | the brackets [] scliding up a list - in this case start a No. 1 until infinity
#    print("hello", argument)

#f = Figlet(font='italic')
print(sys.argv)
f = sys.argv[2]
t = input("Input: ")
print(f.renderText(t))
