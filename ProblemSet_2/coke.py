
while True:
    price = int(50)
    pay = int(input("Amount Due: "))
    payed = price - pay
    print(payed)
    if payed <= price:
        break

