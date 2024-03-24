# Object-Oriented Programming

# Tuple
# (variable1, variable2) is a tuple

def main():
    student = get_student()
    print(f'{student[0]} is in {student[1]}')

def get_student():
    name = input('Name:')
    house = input('House:')
    return (name, house) #is a tuple (is not mutable)
    #return [name,house] #is a list (is mutable)
