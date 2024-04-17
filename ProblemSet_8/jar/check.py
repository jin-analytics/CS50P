class Jar:
    def __init__(self, initial_amount, eating_amount):
        self.initial_amount = initial_amount
        self.eating_amount = eating_amount

    def __str__(self):
        return f"At the beginning are {self.initial_amount} cookies in the jar..."


    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if int(size) > int(self.initial_amount):
            raise ValueError
        self.size = size

def main():
    print(get_cookies())

def get_cookies():
    initial_amount = input("How many cookies to the jar?")
    eating_amount = input("How many cookies will be eaten from the jar?")
    return Jar(initial_amount, eating_amount)

if __name__ == "__main__":
    main()
