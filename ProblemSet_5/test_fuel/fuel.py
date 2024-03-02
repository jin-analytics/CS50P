def main():
    while True:
            fraction = input("Fraction: ").split("/") # expects Format "X/Y"
            if convert(fraction) != False:
                percentage = round(convert(fraction))
                percentage = gauge(percentage)
                if percentage.isdigit():
                    #print(f"{percentage}%", sep="")
                    print(percentage)
                    return True
                else:
                    print(percentage)
                return True


def convert(fraction):
    # Checks if x and y is a number, then divides it to get the percentage of the fraction
    try:
        if len(fraction) != 2:
            return False
        x = int(fraction[0])
        y = int(fraction[1])
        if x > y:
            return False
        elif x == 0:
            percentage = 0.000000001
            return percentage
        else:
            percentage = round((x/y)*100)
            #return isinstance(percentage, int)
            return percentage
    except ZeroDivisionError:
        return False
    except ValueError:
        return False


def gauge(percentage):
    try:
        if 1 < percentage < 99:
            g = str(f"{percentage}%")
            return g
        elif percentage <= 1:
            g = ("E")
            return g
        elif 99 <= percentage <= 100 :
            g = ("F")
            return g
        else:
            return False
    except UnboundLocalError:
        return False


if __name__ == "__main__":
    main()
