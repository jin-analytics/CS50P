from tabulate import tabulate
import os
import sys

#finds the path of the input from the commandline and returns it
def find_files(filename, search_path):
   result = []
   for root, dirs, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

# uses input from commandline and then gives first entree from list
rootdir = os.getcwd() #gets current working directory from commandline
print(os.getcwd())
folder = find_files(sys.argv[1],rootdir) #searches for file from commandline and directory from commandline
folder = folder[0] #returns the first entree of a file which was found

with open(sys.argv[1]) as p:
    print(p.readlines())
