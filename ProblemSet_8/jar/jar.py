class Jar:
    def __init__(self, size=0, capacity=12):
        self.size = size
        self.capacity = capacity

    def __str__(self):
        s = str_append_list_join("🍪", self.size)
        return f"{s}"


    def deposit(self, n):
        self.size = self.size + n
        #self.deposit = deposit

    def withdraw(self, n):
        self.size = self.size - n
        #self.withdraw = withdraw

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
        if (self._size) < 0:
            raise ValueError
        elif int(self._size) > int(self.capacity):
            raise ValueError


def main():
    cookies = Jar()
    cookies.deposit(30)
    cookies.withdraw(5)
    print(cookies)

def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()

