
def main():
    greeting = input("Greeting: ")
    print("$",value(greeting))


def value(greeting):
    # Split it in a matrix (1 x n) to select the first "Hello"
    greeting = greeting.split()
    match greeting:
    # Select different types of hello in the first column of the matrix...
    # ... with *rest will be the rest of the column entrees ignored!
        case ["Hello," | "Hello" | "hello", *rest]:
            #print("$0")
            val = int(0)
        case _:
        # Joing the matrix back together, so that you can...
        # ... select the letter and not the full word!
            greeting = ' '.join(greeting)
            print(greeting[0])
            if greeting[0] == "H" or "h":
                #print("$20")
                val = int(20)
            else:
                print("$100")
                val = int(100)
    return val

if __name__ == "__main__":
    main()
