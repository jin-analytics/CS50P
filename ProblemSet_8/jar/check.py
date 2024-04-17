class Jar:
    # __init__ initilizes the capacity of the cookie jar
    # when "capacity" is not positive, raises ValueError
    def __init__(self, capacity=12):
         if capacity < 0:
            raise ValueError('Negative capacity')
        #self.capacity = capacity



def main():
    print(get_cookies())


def get_cookies():
    in_jar = input("How many cookies to the jar?")
    jar = Jar(in_jar)
    return jar

if __name__ == "__main__":
    main()
