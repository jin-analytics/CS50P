# Get whatever greeting
greeting = input().split()
print(greeting)

match greeting:
    case ["hello" | "Hello"]:
        print("$100")
