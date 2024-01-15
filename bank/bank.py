# Capatalize the first letter
greeting = input("Greeting: ")

# Get whatever greeting and split it in a matrix (1 x n) | n= number of words
greeting = greeting.split()

match greeting:
    case ["Hello," | "Hello" | "hello", *rest]:
        print("$0")
    case _:
        greeting = ' '.join(greeting)
        if greeting[0] == "H":
            print("$20")
        else:
            print("$100")



