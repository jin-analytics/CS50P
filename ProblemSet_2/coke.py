
price = int(50)

while True:
    print("Amount Due: ", price)
    pay = int(input("Insert Coin: "))
    price = price - pay
    print("Amount Due: ", price)
    if price >= 50:
        break

