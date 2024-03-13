students = []

with open("before.csv") as csvfile:

### Option 1 - Read out every single line, split it by comma and append to an empty list
    for line in csvfile:
        #name, house = line.rstrip().split(",")
        line = line.rstrip().split(",")
        #line = line[0].split(",")
        print(line)
