from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
   check_for_correct_input(sys.argv)
   filename = check_for_correct_extension_and_file_names(sys.argv)
   #sys.exit(filename)
   try:
      #open image
      Image.open(sys.argv[1])

      #fit image

      #paste image

      #save image

   except FileNotFoundError:
      sys.exit('Input does not exist')



   # width = Image.open("shirt.png").width #get the width of the image which has to be overlayed
   # height = Image.open("shirt.png").height #get the height of the image which has to be overlayed



















def check_for_correct_input(input):
   #print(input)
   if len(input) < 3:
      sys.exit("Too few command-line arguments")
   elif len(input) > 3:
      sys.exit("Too many command-line arguments")
   elif input[1][-4:] != input[2][-4:]:
      sys.exit("Input and output have different extensions")

def check_for_correct_extension_and_file_names(input):
   for elements in input[1:]:
      text, extension = os.path.splitext(elements)
      if extension not in ['.jpg','.jpeg','.png']:
         sys.exit('Invalid output')
   # returns last filename of "input" ... the suggested output
   return text

if __name__ == "__main__":
    main()
