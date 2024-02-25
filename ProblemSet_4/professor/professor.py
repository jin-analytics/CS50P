import random


def main():
    get_level()

def get_level():
    while True:
        try:
            lev = int(input("Level: "))
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
