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
size2 = (200,200) # crop size tupel

for f in os.listdir('.'):
    # checks if image from cmd line is in the current path, then crops it and then saves under new name with _cropped in it
    if f.endswith('.jpg') and f == sys.argv[1]:
        img1 = Image.open(f)
        img1 = ImageOps.fit(image1, size, bleed=0.0, centering=(0.5, 0.5))
        filename1, filetype1 = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
        img1.save('{}_cropped{}'.format(filename1,filetype1)) #saves as 'before1_cropped.png'

    # checks if image from cmd line is in the current path, then crops it and then saves under new name with _cropped in it
    elif f.endswith('.png') and f == sys.argv[2]:
        img2 = Image.open(f)
        img2 = ImageOps.fit(image2, size, bleed=0.0, centering=(0.5, 0.5))
        filename2, filetype2 = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
        img2.save('{}_cropped{}'.format(filename2,filetype2)) #saves as 'before1_cropped.jpg'

img1 = Image.open('{}_cropped{}'.format(filename1,filetype1))
img2 = Image.open('{}_cropped{}'.format(filename2,filetype2))

back_img = img1.copy()
#back_img.paste(img2)
back_img.alpha_composite(img1)
back_img.save(f'{filename1}_cropped_paste.png')


#im1 = Image.open('data/src/rocket.jpg')
#im2 = Image.open('data/src/lena.jpg')

#back_im = im1.copy()
#back_im.paste(im2)
#back_im.save('data/dst/rocket_pillow_paste.jpg', quality=95)
