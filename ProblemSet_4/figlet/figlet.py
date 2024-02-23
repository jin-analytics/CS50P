import sys


if len(sys.argv) <2:
    sys.exist("too few")

for arg in sys.argv[1:]:
    print("hello", arg)

#print(sys.argv[1])
