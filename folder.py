import os
import sys

os.chdir("/workspaces/155905672")

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)
