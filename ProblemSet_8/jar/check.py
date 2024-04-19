class Jar:
    def __init__(self,deposit, withdraw, size=0,  capacity=12):
         if capacity < 0:
            raise ValueError
        self.deposit = deposit
        self.withdraw = withdraw
        self.size = size
        self.capacity = capacity


    def __str__(self):
        ...

    #def deposit(self, n):
    #    ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    #get_cookies()
    cookies = Jar(5, 3)
    print(Jar.cookies)

def get_cookies():
    cookies = Jar(5, 3)
    return cookies

def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()

