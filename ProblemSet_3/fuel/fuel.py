def main():
    fraction = input("Fraction: ")
    x_y_splitter(fraction)

def x_y_splitter(f):
    f = f.split("/")
    print(f)

main()
