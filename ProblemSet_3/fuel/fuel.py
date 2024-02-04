def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)

def calculator(f):
    try:
        if f[0].isdigit() and f[1].isdigit() == True:
            percentage = (int(f[0])/int(f[1]))*100
    except ZeroDivisionError:
        return False

    try:
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
    except UnboundLocalError:
        return False


main()
