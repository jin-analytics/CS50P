from PIL import Image
import sys

#Open the input with Image.open
#resize and crop the input with ImageOps.fit
#using default values for method, bleed, and centering, overlay the shirt with Image.paste
#and save the result with Image.save

PIL.Image.open(sys.argv[1], mode='r', formats=None)

