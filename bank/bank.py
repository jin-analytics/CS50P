# Get whatever greeting
greeting = input().split()
print(greeting)

match greeting:
    case ["hello" | "Hello", *rest]:
        print("$100")
