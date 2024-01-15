# Get input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

def fortytwo(input):
    match input:
    case "42" | "forty-two" | "forty two"
    input = true

    case _:
    input = false

    return input
