import sys
from pyfiglet import Figlet
import pyfiglet
import random

# gets the list of usable fonts
randomfont= pyfiglet.FigletFont.getFonts()
# gets the length of the fontlist
l = len(randomfont)
# choose random number of font list
z = random.randint(0,l)
# use the font with the random number
font = randomfont[z]

if len(sys.argv) > 2:
    sys.exit("too many arguments") # sys.exit | exits the program

#for argument in sys.argv[1:]: # Slices | the brackets [] scliding up a list - in this case start a No. 1 until infinity
#    print("hello", argument)


elif len(sys.argv) == 2: #if "python figlet.py -f font"
#print(sys.argv)
    f = Figlet(font = sys.argv[2])
    text = input("Input: ")
    print(f.renderText(text))

elif len(sys.argv) < 2: #if only "python figlet.py"
    text = input("Input: ")
    f = Figlet(font = randomfont)
    print(f.renderText(text))

else:
    exit()
