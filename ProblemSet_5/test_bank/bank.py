greeting = input("Greeting: ")

# Split it in a matrix (1 x n) to select the first "Hello"
greeting = greeting.split()

match greeting:
    # Select different types of hello in the first column of the matrix...
    # ... with *rest will be the rest of the column entrees ignored!
    case ["Hello," | "Hello" | "hello", *rest]:
        print("$0")
    case _:
        # Joing the matrix back together, so that you can...
        # ... select the letter and not the full word!
        greeting = ' '.join(greeting)
        if greeting[0] == "H":
            print("$20")
        else:
            print("$100")

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
