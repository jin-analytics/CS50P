from PIL import Image
from PIL import ImageOps
import sys
import os

# call like this: image_fusion(background_filename, background_filetype, foreground_filename, foreground_filetype)
# purpose: returns image with filename "{filename2}_{}'."
def image_fusion(filename1,filetype1,filename2,filetype2):

    background = Image.open('{}_cropped{}'.format(filename1,filetype1))
    foreground = Image.open('{}_cropped{}'.format(filename2,filetype2))

    # lays foreground picture over background picture
    background.paste(foreground, (0, 0), foreground.convert('RGBA')) #paste(foreground picture, (x,y), applied mask (here 'RGBA' cause of PNG) )
    background.save('{}_overlayed{}'.format(filename2,filetype2)) #saves as 'filename2_overlayed.png'
    image = Image.open('{}_overlayed{}'.format(filename2,filetype2))

    return image
