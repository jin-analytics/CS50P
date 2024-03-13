students = []

with open("before.csv") as csvfile:
    next(csvfile)
### Option 1 - Read out every single line, split it by comma and append to an empty list
    for line in csvfile:
        #name, house = line.rstrip().split(",")
        line = line.replace('"', '')
#        line = line.rstrip().split(",")
#        students.append(line)
#    print(students[0])
        line = line.rstrip().split(",")
        students.append(line)
