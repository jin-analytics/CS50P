# Purpose:
# In a file called lines.py, implement a program that expects exactly one command-line argument,
# ...the name (or path) of a Python file, and outputs the number of lines of code in that file,
# ...excluding comments and blank lines.

# Condition:
# If the user does not specify exactly one command-line argument,
# ...or if the specified file’s name does not end in .py,
# ...or if the specified file does not exist,
# ...the program should instead exit via sys.exit.

import sys
import os

#finds the path of the input from the commandline and returns it
def find_files(filename, search_path):
   result = []
   for root, dirs, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result


def main():
    counter = [] #empty list which raises when in the readen file is a command or empty line

    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")

        # uses input from commandline and then gives first entree from list
        rootdir = os.getcwd() #gets current working directory from commandline
        folder = find_files(sys.argv[1],rootdir) #searches for file from commandline and directory from commandline
        folder = folder[0] #returns the first entree of a file which was found

        with open(folder, 'r') as f:
            content = f.readlines() # gives the number of written lines in the file
            for line in content:
                line = line.strip(' ') # removes whitespace, so that a comment getzs detected even with tabs used
                if line == '\n':       # subtract a empty line in line 49 
                    counter.append(1)
                elif line[0] == '#':   # substract a commented line in line 49
                    counter.append(1)

            print(len(content) - len(counter))
            sys.exit()
    except EOFError:
        sys.exit()
    except FileNotFoundError:
        sys.exit('File does not exist')
    except IndexError:
        sys.exit('File does not exist')


if __name__ == "__main__":
    main()
