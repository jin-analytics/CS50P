from PIL import Image
from PIL import ImageOps
import sys
import os

def image_crop(x,y,image_name):
    #print('......',image_name)
    try:
        image = Image.open(image_name)
        size = (int(x),int(y)) # crop size tupel
        for f in os.listdir('.'):
            if f == image_name:
                # checks if image from cmd line is in the current path, then crops it and then saves under new name  "{filename}_cropped{filetype}"
                img = Image.open(f)
                img = ImageOps.fit(image, size, bleed=0.0, centering=(0.5, 0.5))
                filename, filetype = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
                img.save('{}_cropped{}'.format(filename,filetype)) #saves as 'before1_cropped.png'#
                image = Image.open('{}_cropped{}'.format(filename,filetype))
                image_name = '{}_cropped{}'.format(filename,filetype)
                return image_name
    except FileNotFoundError:
        sys.exit("Input does not exist")
