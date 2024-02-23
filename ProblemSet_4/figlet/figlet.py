import sys
import Figlet

#Font: italic


if len(sys.argv) <2:
    sys.exit("too few") # sys.exit | exits the program

for argument in sys.argv[1:]: # Slices | the brackets [] scliding up a list - in this case start a No. 1 until infinity
    print("hello", argument)


