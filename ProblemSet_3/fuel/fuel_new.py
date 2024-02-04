def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)

def calculator(f):
    # if x and y is a number, the program calculates how much fuel is left, else it reprompts
    try:


main()
