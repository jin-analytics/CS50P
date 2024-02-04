# asks for input like "x/y", if not this type the program stops otherwise it goes in function calculator()
def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)

def calculator(f):
    # if x and y is a number, the program calculates how much fuel is left, else it reprompts
    if f[0].isdigit() and f[1].isdigit() == True:
        if f[1] == "0" or f[0] < f[1]:
            return False
        percentage = (int(f[0])/int(f[1]))*100
        # if y is a zero or x is greater than y the program repromts


        if 1 < percentage < 99:
            print(round(percentage), "%", sep="")
            exit()
        elif percentage <= 1:
            print("E")
            exit()
        elif percentage <= 99:
            print("F")
            exit()
        else:
            return False

main()
