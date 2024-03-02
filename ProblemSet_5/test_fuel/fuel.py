def main():
    while True:
            fraction = input("Fraction: ").split("/") # expects Format "X/Y"
            if convert(fraction) != False:
                percentage = convert(fraction)
                percentage = gauge(percentage)
                if percentage.isdigit():
                    print(f"{percentage}%", sep="")
                    return True
            else:
                print(percentage)
                return True

def convert(f):
    # Checks if x and y is a number, then divides it to get the percentage of the fraction
    try:
        if len(f) != 2:
            return False
        x = int(f[0])
        y = int(f[1])
        if x > y:
            return False
        else:
            percentage = round((x/y)*100)
            return percentage
    except ZeroDivisionError:
        return False
    except ValueError:
        return False


def gauge(percentage):
    try:
        # ]1%;99%[ print the actual number
        if 1 < percentage < 99:
            #print(round(percentage), "%", sep="")
            #exit()
            g = str(percentage)
            return g
        # <= 1% prints E for Empty
        elif percentage <= 1:
            g = ("E")
            return g
        # <= 99% prints F for Full
        elif 99 <= percentage <= 100 :
            g = ("F")
            return g
        else:
            return False
    except UnboundLocalError:
        return False


if __name__ == "__main__":
    main()
