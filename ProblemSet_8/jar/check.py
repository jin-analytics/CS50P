class Jar:
    def __init__(self, initial_amount, deposit, withdraw):
        self.initial_amount = initial_amount
        self.deposit = deposit
        self.withdraw = withdraw

    def __str__(self):
        cookies_left = int(self.deposit) - int(self.withdraw)
        c  = []
        for _ in range(cookies_left):

            #c = "🍪"
            c = c.append("🍪")
        #return f"Out of {self.deposit} cookies where {self.withdraw} cookies eaten... {cookies_left} left"
        return f"{c} 🍪"


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

def str_append_list_join("🍪", cookies_left):
    l1 = []
    i = 0
    while i < n:
        l1.append(s)
        i += 1
    return ''.join(l1)

if __name__ == "__main__":
    main()
