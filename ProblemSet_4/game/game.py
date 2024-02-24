import random

while True:
    try:
        lev = input("Level: ")
        num = random.randint(1,lev)
        print(num)
    except EOFError:
        exit()
