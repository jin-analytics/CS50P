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

#rootdir = os.getcwd()
#folder = find_files(sys.argv[1],rootdir)
#folder = folder[0]

with open(sys.argv[1]) as p:
    for entrees in p:
        #print(p.readlines())
        print(p[1])
       #print(tabulate(p))
       #print(tabulate(p, headers=["1","2", "3"]))
