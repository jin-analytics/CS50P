import random


def main():
    level = get_level()
    generate_integer(level)

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
    #_________Level 1_________
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
        #print(x,"+",y,"=")
        exercise = str((x,"+",y,"="))
        int(input(exercise))


    #_________Level 2_________
    elif level == 2:
        x = random.randint(1,99)
        y = random.randint(1,99)
        #print(x,"+",y,"=")
        int(input(x,"+",y,"="))

    #_________Level 3_________
    elif level == 3:
        x = random.randint(1,999)
        y = random.randint(1,999)
        #print(x,"+",y,"=")
        int(input(x,"+",y,"="))

if __name__ == "__main__":
    main()
