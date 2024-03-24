# Object-Oriented Programming

#______________________________________________________________________
# Tuple
# (variable1, variable2) is a tuple

def main():
    student = get_student()
    print(f'{student["name"]} is in {student["house"]}')

def get_student():
    name = input('Name:')
    house = input('House:')
    return (name, house) #is a tuple (is not mutable)
    #return [name,house] #is a list (is mutable)

def get_student():
    #student = {}
    #student['name'] = input('Name: ')
    #student['house'] = input('House: ')
    #return student
    name = input('Name:')
    house = input('House:')
    return {'name': name, 'house': house} #is a dict (is mutable)



#______________________________________________________________________
# classes

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f'{student.name} is in {student.house}')

def get_student():
     student = Student()                #   creates an object from a class
     #student.name = input("Name: ")     #   attribute
     #student.house = input("House: ")   #   attribute
     name = input("Name: ")     #   attribute
     house = input("House: ")   #   attribute
     student = Student(name, house)
     return student
