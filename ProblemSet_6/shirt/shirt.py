from PIL import Image
from PIL import ImageOps
import sys

#Open the input with Image.open
#resize and crop the input with ImageOps.fit
#using default values for method, bleed, and centering, overlay the shirt with Image.paste
#and save the result with Image.save

image = Image.open(sys.argv[1], mode='r', formats=None)
size = 128, 128
ImageOps.fit(image, size, bleed=0.0, centering=(0.5, 0.5))
