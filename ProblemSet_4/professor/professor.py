import random


def main():


    level = get_level()
    while True:
        try_counter = []
        numbers = generate_integer(level)
        x = numbers[0]
        y = numbers[1]
        solution = x + y
        try:
            while True:
                print(x,"+",y,"= ", end = "")
                guess = int(input())
                if guess != solution: # when the guess doesn't equal the solution, Errormessage "EEE" appears
                    print("EEE")
                    try_counter.append(0) # you have three guesses, then the program shows the correct answer and stops
                    if len(try_counter) == 3:
                        print(x,"+",y,"= ",solution)
                        break
                else:
                    break
        except ValueError:
            print("", end = "")
        except EOFError:
            return False

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
