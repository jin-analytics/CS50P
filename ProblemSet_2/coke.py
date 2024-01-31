# Initial price is 50 cent
price = int(50)
# Asks for the initial amount which is 50
print("Amount Due:", price)

# as long the price which has to be payed is bigger than 0, the loop continues
while True:
    # insert a coin
    pay = int(input("Insert Coin: "))
    # calculates the price which has to be paid after inserting the coin
    price = price - pay

    if price > 0:

        print("Amount Due:", price)
    # if the paid amount is 50 or more, the lopp stops
    elif price <= 0:
        print("Change Owed:", -1*(price))
        break

