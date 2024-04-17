class Jar:
    # __init__ initilizes the capacity of the cookie jar
    # when "capacity" is not positive, raises ValueError
    def __init__(self, capacity=12):
         if capacity < 0:
            raise ValueError('Negative capacity')
        self.capacity = capacity

    # __str__ returns a string with n times "🍪" in the jar
    def __str__(self):
        return f"{self.capacity} 🍪"


    # deposit should add n cookies to the cookie jar
    # if capacity gets exceeded, raise ValueError
    @property.setter
    def deposit(self, n):
        put_cookies_to_jar = int(input("How many cookies to the jar?"))
        self._n = n


    # withdraw removes n cookies from the cookie jar
    # if there are not enough cookies, raise ValueError
    #@property.setter
    def withdraw(self, n):
        self._n = n

    # returns the capacity of the cookie jar
    @property
    def capacity(self):
        ...

    # size should return the actual amount of cookies in the jar
    # initially 0 inside
    @property
    def size(self):
        ...


def main():
    print(get_cookies())


def get_cookies():
    in_jar = input("How many cookies to the jar?")
    out_jar = input("How many cookies eating?")
    jar = Jar(in_jar, out_jar)
    return jar

if __name__ == "__main__":
    main()
