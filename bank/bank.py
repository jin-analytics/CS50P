# Get whatever greeting
greeting = input()

match greeting:
    case greeting == "hello":
        print("$0")
    case _:
        if greeting[0] == "h":
        print("$20")
