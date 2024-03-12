import os
import sys

#os.chdir("/workspaces/155905672")

rootDir = os.getcwd()
fileToSearch = sys.argv[1]

for files, dirs in os.walk(rootDir,fileToSearch):

#print(os.path.join("/workspaces/155905672", sys.argv[1]))
#print(os.walk("/workspaces/155905672"))

#print(os.path.isfile(sys.argv[1]))
