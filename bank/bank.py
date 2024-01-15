# Get whatever greeting
greeting = input()

match greeting:
    case "hello":
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        else:
            print("$100")
