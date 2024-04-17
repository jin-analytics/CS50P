class Jar:
    def __init__(self, initial_amount):
        self.initial = initial_amount

def main():
    print(get_cookies())

def get_cookies():
    initial_amount = input("How many cookies to the jar?")
    #jar = Jar(initial)
    return Jar(initial_amount)

if __name__ == "__main__":
    main()
