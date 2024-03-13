from PIL import Image
from PIL import ImageOps
import sys
import os
from img_fusion import image_fusion
from img_crop import image_crop

# convert to png, because the jpeg format doesnt contains the transperency information
#JPEG does not support the alpha channel (transparency) that is part of the RGBA color space.
#When you try to save an RGBA image as a JPEG, the alpha channel information will be lost.
def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".jpg":
            sys.exit("Invalid Output")
        elif sys.argv[2][-4:] == ".jpg" and sys.argv[3][-4:] ==".png":
            sys.exit("Input and output have different extensions")

        filename1 = image_crop(300,300,sys.argv[1])
        filename2 = image_crop(300,300,"shirt.png")
        #filename2 = image_crop(300,300,sys.argv[2])
        image = image_fusion(filename1,filename2)
        image.save(sys.argv[2]) #saves as 'filename2_overlayed.png'

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    except IndexError:
        sys.exit('File does not exist')


if __name__ == "__main__":
    main()
