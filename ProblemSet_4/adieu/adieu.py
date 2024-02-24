adieulist = {} #creates empty dictionary which will be filled in the while loop


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the dictionary "adieulist"
            #if the product doesnt exist in the "einkaufsliste", then product gets value 1
            #else the value of the product gets increased by 1
            if adieulist.get(n) == None:
                adieulist[n] = 1
            else:
                adieulist[n] = adieulist.get(n) + 1

        except EOFError:
            print(f"Adieu, adieu, to {n}")








if __name__ == "__main__":
    main()
