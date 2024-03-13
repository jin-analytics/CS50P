from PIL import Image
from PIL import ImageOps
import sys
import os

#Open the input with Image.open
#resize and crop the input with ImageOps.fit
#using default values for method, bleed, and centering,
#overlay the shirt with Image.paste
#and save the result with Image.save

#with open(Image.open(sys.argv[1], mode='r', formats=None)) as image:
#    size = 128, 128
#    ImageOps.fit(image, size, bleed=0.0, centering=(0.5, 0.5))
#    Image.paste(sys.argv[2], box=None, mask=None)


# convert to png, because the jpeg format doesnt contains the transperency information
#JPEG does not support the alpha channel (transparency) that is part of the RGBA color space.
#When you try to save an RGBA image as a JPEG, the alpha channel information will be lost.

image1 = Image.open(sys.argv[1])
image2 = Image.open(sys.argv[2])

size = (300,300) # crop size tupel

for f in os.listdir('.'):
    if f.endswith('.jpg') and f == sys.argv[1]:
        image = Image.open(f)
        image = ImageOps.fit(image1, size, bleed=0.0, centering=(0.5, 0.5))
        filename, filetype = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
        image.save('{}_cropped{}'.format(filename,".png")) #saves as 'before1_cropped.png'

    elif f.endswith('.png') and f == sys.argv[2]:
        image = Image.open(f)
        image = ImageOps.fit(image1, size, bleed=0.0, centering=(0.5, 0.5))
        filename, filetype = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
        image.save('{}_cropped{}'.format(filename,filetype)) #saves as 'before1_cropped.jpg'

