# Capatalize the first letter
greeting = input().capitalize()
# Get whatever greeting and split it in a matrix (1 x n) | n= number of words
greeting = greeting.split()

match greeting:
    case ["hello" | "Hello", *rest]:
        print("$0")
    case _:
        if greeting[0] == "H":
            print("$20")
        else:
            print("$100")

greeting = ' '.join(greeting)

