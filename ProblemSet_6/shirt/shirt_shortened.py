from PIL import Image
from PIL import ImageOps
import sys
import os
# convert to png, because the jpeg format doesnt contains the transperency information
#JPEG does not support the alpha channel (transparency) that is part of the RGBA color space.
#When you try to save an RGBA image as a JPEG, the alpha channel information will be lost.
def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != sys.argv[2][-4:]:
           sys.exit("Input and output have different extensions")
        while True:
            if sys.argv[1][-4:] != ".png":
                break
            elif sys.argv[1][-4:] != ".jpg":
                break
            elif sys.argv[1][-5:] != ".jpeg":
                break
            else:
                sys.exit()

        width = Image.open("shirt.png").width #get the width of the image which has to be overlayed
        height = Image.open("shirt.png").height #get the height of the image which has to be overlayed

        filename1 = image_crop(width,height,sys.argv[1])
        filename2 = image_crop(width,height,"shirt.png")
        #filename2 = image_crop(300,300,sys.argv[2])
        image = image_fusion(filename1,filename2)
        image.save(sys.argv[2]) #saves as 'filename2_overlayed.png'
        Image.open(sys.argv[2])
        sys.exit()

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    #except IndexError:
     #   sys.exit('File does not exist')



def image_crop(x,y,image_name):
    #print('......',image_name)
    try:
        image = Image.open(image_name)
        size = (int(x),int(y)) # crop size tupel
        for f in os.listdir('.'):
            if f == image_name:
                # checks if image from cmd line is in the current path, then crops it and then saves under new name  "{filename}_cropped{filetype}"
                img = Image.open(f)
                img = ImageOps.fit(image, size)
                filename, filetype = os.path.splitext(f) #filename zB 'before1' & filetype zB '.jpg'
                img.save('{}_cropped{}'.format(filename,filetype)) #saves as 'before1_cropped.png'#
                image = Image.open('{}_cropped{}'.format(filename,filetype))
                image_name = '{}_cropped{}'.format(filename,filetype)
                return image_name
    except FileNotFoundError:
        sys.exit("Input does not exist")




if __name__ == "__main__":
    main()
