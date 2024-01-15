# Get whatever greeting
greeting = input().split()
#print(greeting)
#greeting = greeting.replace(' ','')

match greeting:
    case ["hello" | "Hello", *rest]:
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        else:
            print("$100")

