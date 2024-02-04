# len interprets how many entrees are inside "fruits" and range uses this number to iterate n times, with n= amount of entrees
#def print_fruit_list():
#    fruits = ["apple","avocado","banana"]
#    for i in range(len(fruits)):
#        print(i+1,fruits[i])
#print_fruit_list()
#_______________________________________________________________________________________________________________________________

# Actual Problem solution of nutrition.py:
def main():
    #while True:
        item = input("Item: ").lower()
        calories(item)
        #if calories(item) == True:
            #break


def calories(item):

    # list of top20 consumed fruits in the US
    fruits = [
        {"ranking place": "1","fruit name": "apple","calories":"130"},
        {"ranking place": "2","fruit name": "avocado","calories":"50"},
        {"ranking place": "3","fruit name": "banana","calories":"110"},
        {"ranking place": "4","fruit name": "cantaloupe","calories":"50"},
        {"ranking place": "5","fruit name": "grapefruit","calories":"60"},
        {"ranking place": "6","fruit name": "grapes","calories":"90"},
        {"ranking place": "7","fruit name": "honey melon","calories":"50"},
        {"ranking place": "8","fruit name": "kiwifruit","calories":"90"},
        {"ranking place": "9","fruit name": "lemon","calories":"15"},
        {"ranking place": "10","fruit name": "lime","calories":"20"},
        {"ranking place": "11","fruit name": "nectarine","calories":"60"},
        {"ranking place": "12","fruit name": "orange","calories":"80"},
        {"ranking place": "13","fruit name": "peach","calories":"60"},
        {"ranking place": "14","fruit name": "pear","calories":"100"},
        {"ranking place": "15","fruit name": "pineapple","calories":"50"},
        {"ranking place": "16","fruit name": "plums","calories":"70"},
        {"ranking place": "17","fruit name": "strawberries","calories":"50"},
        {"ranking place": "18","fruit name": "sweet cherries","calories":"100"},
        {"ranking place": "19","fruit name": "tangerine","calories":"50"},
        {"ranking place": "20","fruit name": "watermelon","calories":"80"},
    ]

    for fruit in fruits:
        if item == fruit["fruit name"]:
            print("Calories:", fruit["calories"])
            return True



main()
