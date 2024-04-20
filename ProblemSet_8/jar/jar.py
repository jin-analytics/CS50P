class Jar:
    def __init__(self, size=0, capacity=12):
        self.size = size
        self.capacity = capacity

    def __str__(self):
        return str_append_list_join("🍪", self.size)


    def deposit(self, n):
        self.size = self.size + n
        if int(self.size) > int(self.capacity):
            raise ValueError

    def withdraw(self, n):
        self.size = self.size - n
        if int(self.size) < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, c):
        if int(c) < 0:
            raise ValueError
        self._capacity = c

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, s):
        if int(s) < 0:
            raise ValueError
        self._size = s



def main():
    cookies = Jar()
    cookies.deposit(12)
    cookies.withdraw(12)
    print(cookies)
    #cookies.capacity = 12
    #print(cookies.capacity)

def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()

