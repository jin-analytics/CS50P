# Get whatever greeting
greeting = input()

match greeting:
    case "hello" | "Hello":
        print("$0")
    case _:
        if greeting[0] == "h" | "H":
            print("$20")
        else:
            print("$100")


