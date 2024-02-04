# menu list:
menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
        item = input("Item: ")
        if item
        amount = total(item)
        print (format(amount, '.2f'))


def total(i):
    for food in menu:
        if food == i:
            price = float(menu[food])
            print (format(price, '.2f'))
    try:
        while True:
            item = input("Item: ")
            for food in menu:
                if food == item:
                    price = float(menu[food]) + price
                    print (format(price, '.2f'))
    except EOFError:
         return price


main()
