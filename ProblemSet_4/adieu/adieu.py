einkaufsliste = {} #creates empty list which will be filled in the while loop


def main():
    while True:

        try:
            #n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            var = input() #creates variable where user inputs grocerie products
            #if the product doesnt exist in the "einkaufsliste", then product gets value 1
            #else the value of the product gets increased by 1
            if einkaufsliste.get(var) == None:
                einkaufsliste[var] = 1
            else:
                einkaufsliste[var] = einkaufsliste.get(var) + 1

            print(einkaufsliste)

        except EOFError:
            print(f"Adieu, adieu, to {n}")








if __name__ == "__main__":
    main()
