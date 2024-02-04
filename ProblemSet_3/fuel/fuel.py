def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        if len(fraction) == 2:
            calculator(fraction)


        #fraction_calculator(x_y_splitter(fraction))


def calculator(f):
    #print(f)
    if f[0].isdigit() and f[1].isdigit() == True:
        percentage = (int(f[0])/int(f[1]))*100
        if 1 < percentage < 99:
            print(round(percentage), "%", sep="")
            exit()
        elif percentage <= 1:
            print("E")
        else:
            print("F")

    else:
        exit()




main()
