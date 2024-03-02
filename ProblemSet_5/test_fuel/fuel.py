def main():
    while True:
        percentage = convert(input("Fraction: "))
        gauge(percentage)

def convert(fraction):
    # Checks if x and y is a number, then divides it to get the percentage of the fraction
    try:
        if f[0].isdigit() and f[1].isdigit() == True:
            percentage = (int(f[0])/int(f[1]))*100
            return percentage
    except ZeroDivisionError:
        return False


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
