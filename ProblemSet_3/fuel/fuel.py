# asks for input like "x/y", if not this type the program stops otherwise it goes in function calculator()
def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)
        else:
            exit()


        #fraction_calculator(x_y_splitter(fraction))


def calculator(f):
    # if x and y is a number, the program calculates how much fuel is left, else it stops
    if f[0].isdigit() and f[1].isdigit() == True:
        percentage = (int(f[0])/int(f[1]))*100
        if 1 < percentage < 99:
            print(round(percentage), "%", sep="")
            exit()
        elif percentage <= 1:
            print("E")
            exit()
        else:
            print("F")
            exit()
    else:
        exit()


main()
