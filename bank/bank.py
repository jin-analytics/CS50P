# Get whatever greeting
greeting = input().split()
#print(greeting)
#greeting = greeting.replace(' ','')

match greeting:
    case ["hello" | "Hello*, *rest]:
        print("$100")

    case _:
    
