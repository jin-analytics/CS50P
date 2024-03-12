import os

os.chdir("/workspaces/155905672")

for dirpath, dirnames, filenames in os.walk("/workspaces/155905672"):
   # print("Current Path:", dirpath)
   # print("Directories:", dirnames)
    for entrees in filenames:
        #print("Files:", filenames)
        print(entrees)
        print()
