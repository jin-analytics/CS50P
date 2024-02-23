import sys
from pyfiglet import Figlet
import pyfiglet
import random

# gets the list of usable fonts
font = pyfiglet.FigletFont.getFonts()
# gets the length of the fontlist
l = len(font)
# choose random number of font list
z = random.randint(0,l)
# use the font with the random number
font = font[z]

#if len(sys.argv) <2:
#    sys.exit("too few") # sys.exit | exits the program

#for argument in sys.argv[1:]: # Slices | the brackets [] scliding up a list - in this case start a No. 1 until infinity
#    print("hello", argument)

#f = Figlet(font='italic')
if len(sys.argv) = 2: #if "python figlet.py -f font"
#print(sys.argv)
    f = Figlet(font = sys.argv[2])
    t = input("Input: ")
    print(f.renderText(t))

elif len(sys.argv) < 2: #if only "python figlet.py"
    t = input("Input: ")
    #f = Figlet(font = FigletFonts.getFonts())
    print(pyfiglet.FigletFont.getFonts())
