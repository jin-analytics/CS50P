import random


def main():
    level = get_level()
    numbers = generate_integer(level)
    x = numbers[0]
    y = numbers[1]
    solution = x + y
    while True:
        print(x,"+",y,"= ", end = "")
        guess = int(input())
        if guess != solution:
            print("EEE")
        else:
            return True

def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3: #just accepts input of [1;3]
                return lev
        except ValueError:
            print("", end = "")
        except EOFError:
            return False


def generate_integer(level):
    try:
#__________________________________Level 1
        if level == 1:
            x = random.randint(1,9)
            y = random.randint(1,9)
            return x,y
#__________________________________Level 2
        elif level == 2:
            x = random.randint(1,99)
            y = random.randint(1,99)
            return x,y
#__________________________________Level 3
        elif level == 3:
            x = random.randint(1,999)
            y = random.randint(1,999)
            return x,y
    except ValueError:
        print("", end = "")
    except EOFError:
        return False

if __name__ == "__main__":
    main()
