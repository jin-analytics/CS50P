class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

employee1 = Employee('Jakob','Ingwio',100000)

print(Employee.__dict__)

print(employee1.pay)
employee1.apply_raise() # applies the pay raise to __init__ self.pay
print(employee1.pay)
