def main():
    # Initial price is 50 cent
    price = 50
    coin_machine(price)

def coin_machine(price):
    # as long the price which has to be payed is bigger than 0, the loop continues
    while True:
        # insert a coin
        print("Amount Due:", price)
        pay = int(input("Insert Coin: "))
        # accepted coins 25, 10 or 5 cent
        match pay:
            case 25 | 10 | 5:
                price = price - pay
                # if the paid amount is 50 or more, the loop stops
                if price <= 0:
                    print("Change Owed:", -1*(price))
                    break

# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
