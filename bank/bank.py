# Get whatever greeting
greeting = input()
if greeting[0] == " ":
greeting = greeting[0].replace(' ','').lower()
print(greeting)

match greeting:
    case "hello" | "Hello":
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        else:
            print("$100")


