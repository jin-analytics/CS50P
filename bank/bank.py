# Get whatever greeting
greeting = input()
greeting=greeting.split()
print(greeting)
if greeting[0] == " ":
    greeting = greeting[0].replace(' ','')


match greeting:

    case greeting == "hello" | "Hello":
        print("$0")
    case _:
        if greeting[0] == "h":
            print("$20")
        else:
            print("$100")


