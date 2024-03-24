# Object-Oriented Programming

# Tuple
# (variable1, variable2) is a tuple

def main():
    student = get_student()
    print(f'{student[]} is in {student[1]}')

def get_student():
    name = input('Name:')
    house = input('House:')
    return (name, house) #is a tuple (is not mutable)
    #return [name,house] #is a list (is mutable)

def get_student():
    student = {}
    student['name'] = input('Name: ')
    student['house'] = input('House: ')
    return student
