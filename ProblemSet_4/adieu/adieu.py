adieulist = []


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            #print(adieulist)

        except EOFError:
            if len(adieulist) == 1:
              print(len(adieulist))
              print(f"Adieu, adieu, to {adieulist[0]}")

            elif len(adieulist) == 2:
              print(len(adieulist))
              print(f"Adieu, adieu, to {adieulist[0]} and {adieulist[1]}")

            elif len(adieulist) > 2:


            exit()


def 





if __name__ == "__main__":
    main()
