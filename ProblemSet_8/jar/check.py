class Jar:
    def __init__(self, size=0, capacity=12):
        if capacity < 0:
            raise ValueError
        self.size = size
        self.capacity = capacity




    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self.capacity
    #@capacity.setter
    #def capacity(self, new_capa):
    #    self._capacity = new_capa

   # @property
    #def size(self):
     #   ...


def main():
    #get_cookies()
    cookies = Jar()
    print(cookies.size)
    cookies.deposit(5)
    cookies.withdraw(3)
    print(cookies.size)
    print(cookies.capacity)


def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()

