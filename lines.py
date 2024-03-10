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

import sys
import os


filename = sys.argv[1]

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result



















def main():
    print(find_files(sys.argv[1],"ProblemSet_6"))
    counter = [] #empty list which raises when in the readen file is a command or empty line
    while True:
        try:
            filename = 'einstein.py'#sys.argv[1]

            with open(filename, 'r') as f:
                content = f.readlines()
                for line in content:
                    line = line.strip(' ')
                    if line == '\n':
                        counter.append(1)
                    elif line[0] == '#':
                        counter.append(1)

                print(len(content) - len(counter))
                sys.exit()
        except EOFError:
            sys.exit()
        except FileNotFoundError:
            sys.exit('Not found')
        #except EOFError:
        #sys.exit()


if __name__ == "__main__":
    main()
