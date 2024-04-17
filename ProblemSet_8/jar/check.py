class Jar:
    def __init__(self, capacity=12, initial):
         if int(capacity) < 0:
            raise ValueError('Negative capacity')
        #self.capacity = capacity
        self.initial = initial

def main():
    print(get_cookies())

def get_cookies():
    initial = input("How many cookies to the jar?")
    #jar = Jar(initial)
    return Jar(initial)

if __name__ == "__main__":
    main()
