adieulist = []


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            print(adieulist)

        except EOFError:
            print(len(adieulist))
            print(f"Adieu, adieu, to {adieulist[0:len(adieulist)]}")
            exit()








if __name__ == "__main__":
    main()
