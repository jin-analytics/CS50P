# Get whatever greeting and split it in a matrix (1 x n) | n= number of words
greeting = input().split()
# Removes the white space from the first column in the string matrix
greeting[0] = greeting[0].replace(' ','')
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

