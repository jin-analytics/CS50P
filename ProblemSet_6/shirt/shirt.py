from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
   check_for_correct_input(sys.argv)
   filename, extension = check_for_correct_extension_and_file_names(sys.argv)
   #sys.exit(filename)
   try:
      #open image
      img = Image.open(sys.argv[1])

      #get size tupel of image which will be in the foreground
      size = Image.open("shirt.png").size
      #width = Image.open(sys.argv[1]).width
      #height = Image.open(sys.argv[1]).height

      #fit image from background to the one from foreground
      img = ImageOps.fit(img, size)

      #paste image
      background = img
      foreground = Image.open("shirt.png")
      #background.paste(foreground, (0, 0), foreground.convert('RGBA')) #paste(foreground picture, (x,y), applied mask (here 'RGBA' cause of PNG) )
      background.paste(foreground, foreground.convert('RGBA')) #paste(foreground picture, (x,y), applied mask (here 'RGBA' cause of PNG) )

      #save image
      background.save('{}{}'.format(filename, extension)) #saves as 'filename2_overlayed.png'
      #image = Image.open("new_" + filename2)


   except FileNotFoundError:
      sys.exit('Input does not exist')



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
   return text, extension



if __name__ == "__main__":
    main()
