import random


def main():
    get_level()

def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3:
                num = random.randint(1,lev)
                print(num)
                break
        except ValueError:
            print("", end = "")
        except EOFError:
            return False


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
