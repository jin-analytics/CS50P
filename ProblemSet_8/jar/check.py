class Jar:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount

    def __str__(self):
        return f"At the beginning are {self.initial_amount} cookies in the jar..."


    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        self.size = size

def main():
    print(get_cookies())

def get_cookies():
    initial_amount = input("How many cookies to the jar?")
    #jar = Jar(initial)
    return Jar(initial_amount)

if __name__ == "__main__":
    main()
