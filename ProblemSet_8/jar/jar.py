class Jar:
    def __init__(self, size, deposit, withdraw, capacity=12):
        #self.initial_amount = initial_amount
        if capacity < 0:
            raise ValueError
        self.size = size
        self.deposit = deposit
        self.withdraw = withdraw
        self.capacity = capacity


    def __str__(self):
        #cookies_left = int(self.deposit) - int(self.withdraw)
        #self.size = int(self.deposit) - int(self.withdraw)
        s = str_append_list_join("🍪", Jar.size)
        #return f"Out of {self.deposit} cookies where {self.withdraw} cookies eaten... {cookies_left} left"
        return f"{s}"

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    #@property
    #def initial_amount(self):
    #    return self._initial_amount
    #@initial_amount.setter
    #def initial_amount(self, initial_amount):
    #    self._initial_amount = initial_amount

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        size = int(Jar.deposit) - int(Jar.withdraw)
        self._size = size


# Deposit of cookies
    @property
    def deposit(self):
        return self._deposit
    @deposit.setter
    def deposit(self, deposit):
        self._deposit = deposit

# Withdraw of cookies
    @property
    def withdraw(self):
        return self._withdraw
    @withdraw.setter
    def withdraw(self, withdraw):
        self._withdraw = withdraw



def main():
    print(get_cookies())

def get_cookies():
    size = 0
    deposit = input("How many cookies to the jar? ")
    withdraw = input("How many cookies will be eaten from the jar? ")
    return Jar(size, deposit, withdraw)

def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()
