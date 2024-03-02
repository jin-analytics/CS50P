def main():
    while True:
        try:
            fraction = input("Fraction: ")
            fraction = fraction.split("/")
            if len(fraction) == 2:
                percentage = convert(fraction)
                gauge(percentage)
        except ValueError:
            return False

def convert(f):
    # Checks if x and y is a number, then divides it to get the percentage of the fraction
    try:
        if f[0].isdigit() and f[1].isdigit() == True:
            percentage = (int(f[0])/int(f[1]))*100
            return percentage
    except ZeroDivisionError:
        return False


def gauge(percentage):
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
        elif 99 <= percentage <= 100 :
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


if __name__ == "__main__":
    main()
