# Get whatever greeting and split it in a matrix (1 x n) | n= number of words
greeting = input().lower()
greeting = input().split()
# Lowers all letters in the first colum of the matrix
print(greeting)

match greeting:
    case ["hello" | "Hello", *rest]:
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        elif greeting[0] == "H":
            print("$20")
        else:
            print("$100")

