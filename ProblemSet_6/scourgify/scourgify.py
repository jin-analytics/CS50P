# make a list with dictionary in it
    # the name is key
    # the house is value
    # draco : slytherin

import csv

def main():
    
    students = []
    # reads the before.csv file and creates a list "students" with this structure: [firstname, lastname, house]
    with open("before.csv") as csvfile:
        next(csvfile)
        for line in csvfile:
            line = line.replace('"', '')
            lastname, firstname, house = line.rstrip().split(",")
            firstname=firstname.replace(' ', '')
            students.append([firstname, lastname, house])

    # writes a new file "after.csv" with the structure from the list "studens" + header "firstname, lastname, house"
    with open("after.csv", "w") as csvfile:
        writer =  csv.writer(csvfile)
        writer.writerow(['first name', 'last name', 'house']) #creates the header in the csv.file
        for firstname, lastname, house in students:
            writer.writerow([firstname, lastname, house])

if __name__ == "__main__":
    main()



















    #print(students)

     #with open("test.csv", "w") as newfile:
     #       for line in
     #       writer =  csv.writer(newfile)
     #       writer.writerow([lastname, firstname, house])




































### Option 1 - Read out every single line, split it by comma and append to an empty list
#    for line in csvfile:
#        row = line.rstrip().split(",")
#        students.append(row)
#    print(students)

### Option 2 - Use the csv.reader() which splits automaticly by comma and append the single lines to an empty list
#    reader = csv.reader(csvfile)
#    for line in reader:
#        students.append(line)
#    print(students)

### Option 3 - Read out every single line, split it by comma and append to an empty dictionary
#    reader = csv.reader(csvfile)
#    for line in reader:
#        students.append(line)#
#       print(students[0], students[1])
    #print(students)
