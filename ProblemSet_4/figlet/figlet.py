import sys
from pyfiglet import Figlet
import pyfiglet
import random

def main():
    # gets the list of usable fonts
    randomfont= pyfiglet.FigletFont.getFonts()
    # gets the length of the fontlist
    l = len(randomfont)
    # choose random number of font list
    z = random.randint(0,l)
    # use the font with the random number
    randomfont = randomfont[z]

    try:
        if len(sys.argv) == 3 and sys.argv[1] == "-f": #if "python figlet.py -f font"
            if fontexist(sys.argv[2]) == True:
                f = Figlet(font = sys.argv[2])
                text = input("Input: ")
                print(f.renderText(text))
            else:
                sys.exit("Invalid usage")

        elif len(sys.argv) == 1: #if only "python figlet.py"
            text = input("Input: ")
            f = Figlet(font = randomfont)
            print(f.renderText(text))

        else:
            sys.exit("Invalid usage")

    except TypeError:
        sys.exit("Invalid usage")

def fontexist(e):
    fontlist = pyfiglet.FigletFont.getFonts()
    for fonts in fontlist:
        if e == fonts:
            return True
    return False

main()




