import os

os.chdir("/workspaces/155905672")

for dirpath, dirnames, filenames in os.walk("/workspaces/155905672"):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()
