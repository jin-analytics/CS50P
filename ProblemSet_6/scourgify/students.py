students = []

with open("before.csv") as csvfile:
    next(csvfile)
### Option 1 - Read out every single line, split it by comma and append to an empty list
    for line in csvfile:
        line = line.replace('"', '')
        lastname, firstname, house = line.rstrip().split(",")
        student = {"firstname":firstname, "lastname":lastname, "house":house}
        students.append(student)
        #print(student["house"],student["firstname"], student["lastname"])
    with open("test.csv") as newfile:
         csv.writer()
