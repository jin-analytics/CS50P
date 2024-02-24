adieulist = []


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            print(adieulist)

        except EOFError:
            print(f"Adieu, adieu, to {n}")








if __name__ == "__main__":
    main()
