class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        #__init__ method runs every time we create a new employee, due to this
        # we can keep track of all iterations
        Employee.num_of_employees += 1

    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


#print('Number of Employees:', Employee.num_of_employees)

employee1 = Employee('Jakob','Ingwio',100000)
employee2 = Employee('Loser','Mustermann',30000)

#employee1.raise_amount = 1.07
#print(employee1.__dict__)
#print('Before adjusting pay raise:',employee1.pay)
#employee1.apply_raise() # applies the pay raise to __init__ self.pay
#print('After adjusting pay raise:',employee1.pay)

#print('Number of Employees:', Employee.num_of_employees)

#print(employee1.raise_amount)
#Employee.set_raise_amount(1.18)
#print(employee1.raise_amount)

emp_str = 'Jako-Ing-100'
print(emp_str)
emp_str = Employee.emp_from_str(emp_str)
print(emp_str.first, emp_str.last, emp_str.pay)

