import random

def main():
    lev = int(input("Level: "))
    num = random.randint(1,lev)

    while True:
        try:
            print(num)
            gue = int(input("Guess: "))

            if gue == num:
                print("Just right!")
                exit()
            elif gue < num:
                print("Too small!")
            elif gue > num:
                print("Too large!")

        except EOFError:
            exit()

if __name__ == "__main__":
    main()
