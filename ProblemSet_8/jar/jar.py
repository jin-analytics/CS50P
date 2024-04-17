class Jar:
    # __init__ initilizes the capacity of the cookie jar
    # when "capacity" is not positive, raises ValueError
    def __init__(self, capacity=12):
        ...

    
    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
