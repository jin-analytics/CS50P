# Get whatever greeting
greeting = input()

match greeting:
case greeting == "hello":
    print("$0")
case greeting[0] == "h":
    print("$20")
