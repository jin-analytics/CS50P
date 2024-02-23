import sys


if len(sys.argv) <2:
    sys.exit("too few") # sys.exit | exits the program

for arg in sys.argv[1:]:
    print("hello", arg)

#print(sys.argv[1])
