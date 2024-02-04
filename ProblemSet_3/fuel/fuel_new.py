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
    #except ValueError:
    #    return False

main()
