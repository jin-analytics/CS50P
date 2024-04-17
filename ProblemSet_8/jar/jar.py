class Jar:
    # __init__ initilizes the capacity of the cookie jar
    # when "capacity" is not positive, raises ValueError
    def __init__(self, capacity=12):
        ...

    # __str__ returns a string with n times "🍪" in the jar
    def __str__(self):
        ...

    # deposit should add n cookies to the cookie jar
    # if capacity gets exceeded, raise ValueError
    def deposit(self, n):
        ...

    # withdraw removes n cookies from the cookie jar
    # if there are not enough cookies, raise ValueError
    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
