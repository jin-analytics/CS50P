adieulist = [] #creates empty list which will be filled in the while loop


def main():
    while True:

        try:
            #n = input("Name: ") #creates variable where the name gets added to the list "adieulist"

            adieulist[input("Name: ")]
            print(adieulist)

        except EOFError:
            print(f"Adieu, adieu, to {n}")








if __name__ == "__main__":
    main()
