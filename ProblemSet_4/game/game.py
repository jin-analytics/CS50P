import random
import sys

def main():
    while True:
        try:
            lev = int(input("Level: "))
            num = random.randint(1,lev)
            break
        except ValueError:
            print("", end = "")
        except EOFError:
            return False

    while True:
        try:
            #print(num)
            gue = int(input("Guess: "))

            if gue == num:
                print("Just right!")
                sys.exit()
            #elif gue < num and gue > 0:
            elif gue < num:
                print("Too small!")
            elif gue > num:
                print("Too large!")

        except EOFError:
            return False
        except ValueError:
            print("", end = "")

if __name__ == "__main__":
    main()
