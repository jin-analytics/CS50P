
price = int(50)
print("Amount Due:", price)

while True:

    pay = int(input("Insert Coin: "))
    price = price - pay
    print("Amount Due:", price)
    if price > 50:
        break

