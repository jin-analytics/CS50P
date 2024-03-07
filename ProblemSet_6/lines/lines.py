# Purpose:
# In a file called lines.py, implement a program that expects exactly one command-line argument,
# ...the name (or path) of a Python file, and outputs the number of lines of code in that file,
# ...excluding comments and blank lines.

# Condition:
# If the user does not specify exactly one command-line argument,
# ...or if the specified file’s name does not end in .py,
# ...or if the specified file does not exist,
# ...the program should instead exit via sys.exit.




### Too few command-line arguments
### Too many command-line arguments
### Not a Python file
### File does not exist

### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
import sys

def main():
    filename = sys.argv[1:]
    #print(filename[1])
    #open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    #f = open(f'{filename[2]}', 'w', encoding="utf-8")
    #with open(f'{filename[2]}', encoding="utf-8") as f:
    #    read_data = f.read()
    #    print(f.readline())
    ##f.readline()

    f = open(f'{filename[2]}', 'r')
    print(f.readline())



if __name__ == "__main__":
    main()
