import os
import sys

os.chdir("/workspaces/155905672")

#print(os.environ.get('HOME'))

#file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
#print(file_path)
print(os.getcwd())
print(os.path.join("/workspaces/155905672", sys.argv[1]))
print(os.walk("/workspaces/155905672"))

#print(os.path.isfile(sys.argv[1]))
