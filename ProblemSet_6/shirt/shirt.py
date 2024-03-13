from PIL import Image
from PIL import ImageOps
import sys
import os
from img_fusion import image_fusion
from img_crop import image_crop
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
def main():
#    image1 = Image.open(sys.argv[1])
#    image2 = Image.open(sys.argv[2])

#    size = (300,300) # crop size tupel

#    for f in os.listdir('.'):
#        # checks if image from cmd line is in the current path, then crops it and then saves under new name with _cropped in it
#        if f.endswith('.jpg') and f == sys.argv[1]:
#            img1 = Image.open(f)
#            img1 = ImageOps.fit(image1, size, bleed=0.0, centering=(0.5, 0.5))
#            filename1, filetype1 = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
#            img1.save('{}_cropped{}'.format(filename1,filetype1)) #saves as 'before1_cropped.png'#
#
#        # checks if image from cmd line is in the current path, then crops it and then saves under new name with _cropped in it
#        elif f.endswith('.png') and f == sys.argv[2]:
#            img2 = Image.open(f)
#            img2 = ImageOps.fit(image2, size, bleed=0.0, centering=(0.5, 0.5))
#            filename2, filetype2 = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
#            img2.save('{}_cropped{}'.format(filename2,filetype2)) #saves as 'before1_cropped.jpg'

    filename1,filetype1 = image_crop(300,300,sys.argv[1])
    filename2,filetype2 = image_crop(300,300,sys.argv[2])
    print(filename1,filetype1)
    #image2 = crop_image(300,300,Image.open(sys.argv[2]))
    #print(image2)
    #print(image1.endswith())
    #image_fusion(filename1,filetype1,filename2,filetype2)
    #image = (image_fusion(filename1,filetype1,filename2,filetype2))
    #image.save("test.png")






if __name__ == "__main__":
    main()
