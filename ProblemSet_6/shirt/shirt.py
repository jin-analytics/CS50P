from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
   check_for_correct_input(sys.argv)
   check_for_correct_extension()
   sys.exit('TUTTO')

#open image
#fit image
#paste image
#save image


def check_for_correct_input(input):
   print(input.split(" "))
   if len(input) < 3:
      sys.exit("Too few command-line arguments")
   elif len(input) > 3:
      sys.exit("Too many command-line arguments")
   elif sys.argv[1][-4:] != sys.argv[2][-4:]:
      sys.exit("Input and output have different extensions")


def check_for_correct_extension():
   pass

if __name__ == "__main__":
    main()
