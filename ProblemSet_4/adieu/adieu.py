adieulist = []


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            print(adieulist)

        except EOFError:
            print()
            print(f"Adieu, adieu, to {adieulist[0:len(adieulist)]}")
            exit()

def 






if __name__ == "__main__":
    main()
