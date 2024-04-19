class Jar:
    def __init__(self, size=0, capacity=12):
        if capacity < 0:
            raise ValueError
        self.size = size
        self.capacity = capacity


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
    def capacity(self, new_capa):
        self._capacity = new_capa

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
        if size < 0:
            raise ValueError


def main():
    #get_cookies()
    cookies = Jar()
    print(cookies.size)
    cookies.deposit(5)
    cookies.withdraw(3)
    print(cookies.size)
    print(cookies.capacity)
    cookies.capacity = '8'
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

