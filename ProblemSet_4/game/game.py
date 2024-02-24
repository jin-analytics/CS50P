import random
import sys

def main():
    while True:
        try:
            lev = int(input("Level: "))
            num = random.randint(1,lev)
            break
        except ValueError:
            print("ups")

    while True:
        try:
            print(num)
            gue = int(input("Guess: "))

            if gue == num:
                print("Just right!")
                sys.exit()
            elif gue < num:
                print("Too small!")
            elif gue > num:
                print("Too large!")

        except EOFError:
            break
        except ValueError:
            print("ups")
        except gue > 1:
            print("ups")

if __name__ == "__main__":
    main()
