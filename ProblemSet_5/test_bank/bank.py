
def main():
    greeting = input("Greeting: ")
    print("$",value(greeting))


def value(greeting):
    # Split it in a matrix (1 x n) to select the first "Hello"
    greeting = greeting.split()
    print(greeting)
    match greeting:
    # Select different types of hello in the first column of the matrix...
    # ... with *rest will be the rest of the column entrees ignored!
        case ["Hello," | "Hello" | "hello", *rest]:
            #print("$0")
            val = int(0)

        case _:
            greeting = ' '.join(greeting)
            if greeting[0] == "H":
                val = int(20)
            elif greeting[0] == "h":
                val = int(20)
            else:
                val = int(100)
    return val

if __name__ == "__main__":
    main()
