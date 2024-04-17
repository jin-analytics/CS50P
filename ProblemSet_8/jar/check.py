class Jar:
    def __init__(self, initial_amount, added_amount, size):
        self.initial_amount = initial_amount
        self.capacity = added_amount
        self.size = size

    def __str__(self):
        return f"At the beginning are {self.initial_amount} cookies in the jar..."


    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if int(size) > int(self.initial_amount):
            raise ValueError
        self._size = size

   

def main():
    print(get_cookies())

def get_cookies():
    initial_amount = 0
    deposit = input("How many cookies to the jar? ")
    size = input("How many cookies will be eaten from the jar? ")
    return Jar(initial_amount, added_amount, size)

if __name__ == "__main__":
    main()
