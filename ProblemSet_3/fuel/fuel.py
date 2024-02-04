# while loop continues until on of the exit() methods will stop the program
# ask for input x/y and then splits it and gives x and y to the calculator() function
def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)


def calculator(f):
    # Checks if x and y is a number, then divides it to get the percentage of the fraction
    try:
        if f[0].isdigit() and f[1].isdigit() == True:
            percentage = (int(f[0])/int(f[1]))*100
    except ZeroDivisionError:
        return False

    try:
        # ]1%;99%[ print the actual number
        if 1 < percentage < 99:
            print(round(percentage), "%", sep="")
            exit()
        # <= 1% prints E for Empty
        elif percentage <= 1:
            print("E")
            exit()
        # <= 99% prints F for Full
        elif percentage >= 99:
            print("F")
            exit()
        # if x = y, for example 100/100, it prints F
        elif f[0] == f[1]:
            print("F")
            exit()
        else:
            return False
    except UnboundLocalError:
        return False

main()
