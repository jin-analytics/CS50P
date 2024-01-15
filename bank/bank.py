# Get whatever greeting
greeting = input()
greeting = greeting[0:2].replace(' ','').lower()

match greeting:
    case "hello" | "Hello":
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        else:
            print("$100")


