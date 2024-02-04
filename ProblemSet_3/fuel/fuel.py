def main():
    while True:
        fraction = input("Fraction: ")
        if x_y_splitter(fraction) == True:
            fraction_calculator()


def x_y_splitter(f):
    f = f.split("/")
    print(f)
    return True

main()
