def main():
    greeting = input("Greeting: ")
    print("$",value(greeting),sep="")

def value(greeting):
    greeting = greeting.replace(",", " ").split()
    match greeting:
    # ... with *rest will be the rest of the column entrees ignored!
        case ["Hello," | "Hello" | "hello", *rest]:
            val = int(0)

        case _:
            greeting = ' '.join(greeting)
            match greeting[0]:
                case "H":
                    val = int(20)
                case "h":
                    val = int(20)
                case _:
                    val = int(100)
    return val

if __name__ == "__main__":
    main()
