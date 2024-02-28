
def main():
    greeting = input("Greeting: ")
    print("$",value(greeting))

def value(greeting):
    greeting = greeting.replace(",", " ").split()
    match greeting:
    # ... with *rest will be the rest of the column entrees ignored!
        case ["Hello," | "Hello" | "hello", *rest]:
            val = int(0)

        case _:
            greeting = ' '.join(greeting)
            if greeting[0] == "H":
                val = int(20)
            elif greeting[0] == "h":
                val = int(20)
            else:
                val = int(100)
    return val

if __name__ == "__main__":
    main()
