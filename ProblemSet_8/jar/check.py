class Jar:
    def __init__(self, initial_amount, deposit, withdraw, capacity=12):
        self.initial_amount = initial_amount
        self.deposit = deposit
        self.withdraw = withdraw
        self.capacity = capacity

    def __str__(self):
        cookies_left = int(self.deposit) - int(self.withdraw)
        s = str_append_list_join("🍪", cookies_left)
        #return f"Out of {self.deposit} cookies where {self.withdraw} cookies eaten... {cookies_left} left"
        return f"{s}, capacity: {self.capacity}"

    @property
    def capacity(self):
        print(f"{self.capacity}")
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


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
    initial_amount = 0
    deposit = input("How many cookies to the jar? ")
    withdraw = input("How many cookies will be eaten from the jar? ")
    return Jar(initial_amount, deposit, withdraw)

def str_append_list_join(add_sign, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(add_sign)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()
