import sys
from pyfiglet import Figlet
from pyfiglet import fonts.zip
# specifying the zip file name
file_name = "my_python_files.zip"
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
# printing all the contents of the zip file
zip.printdir()
# extracting all the files
#Figlet.system("python yourfile.py")

#Font: italic
# example: f = Figlet(font='slant')
# example: print f.renderText('text to render')

#if len(sys.argv) <2:
#    sys.exit("too few") # sys.exit | exits the program

#for argument in sys.argv[1:]: # Slices | the brackets [] scliding up a list - in this case start a No. 1 until infinity
#    print("hello", argument)

#f = Figlet(font='italic')
if len(sys.argv) > 2: #if "python figlet.py -f font"
#print(sys.argv)
    f = Figlet(font = sys.argv[2])
    t = input("Input: ")
    print(f.renderText(t))

elif len(sys.argv) < 2: #if only "python figlet.py"
    t = input("Input: ")
    f = Figlet(font = FigletFonts.getFonts())
