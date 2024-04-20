class Jar:
    def __init__(self, size=0, capacity=12):
        self.size = size
        #self.capacity = capacity
        self._capacity = capacity
        #c = capacity
        #si = size

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
    def capacity(self, c):
        if int(c) > 12:
            raise ValueError
        self._capacity = c

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, c):
        if int(c) < 0:
            raise ValueError
        self._size = c



def main():
    cookies = Jar()
    cookies.deposit(12)
    cookies.withdraw(13)
    print(cookies)
    cookies.capacity = 12
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

