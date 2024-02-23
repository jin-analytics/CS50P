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
randomfont = randomfont[z]

if len(sys.argv) == 3: #if "python figlet.py -f font"
#print(sys.argv)
    f = Figlet(font = sys.argv[2])
    text = input("Input: ")
    print(f.renderText(text))

elif len(sys.argv) == 1: #if only "python figlet.py"
    text = input("Input: ")
    f = Figlet(font = randomfont)
    print(f.renderText(text))

else:
    sys.exit("Invalid usage")
