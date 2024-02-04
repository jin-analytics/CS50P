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
    while True:
        item = input("Item: ")
        amount = total(item)
        print (format(amount, '.2f'))


def total(i):
    for food in menu:
        if food == i:
            #print(menu[food])
            price = float(menu[food])
            return price


main()
