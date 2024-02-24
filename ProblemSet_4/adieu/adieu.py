from name_string import

adieulist = []
def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            #print(adieulist)

        except EOFError:
            if len(adieulist) == 1:
                print()
                print(f"Adieu, adieu, to {adieulist[-len(adieulist)]}") #first entree of somelist[-len(somelist)]

            elif len(adieulist) == 2:
                print()
                print(f"Adieu, adieu, to {adieulist[-len(adieulist)]} and {adieulist[-1]}") #last entree of somelist[-1]

            elif len(adieulist) > 2:
                print()
                print(f"Adieu, adieu, to {name_string(adieulist)}, and {adieulist[-1]}")

            exit()

def name_string(adieulist):
    comma = adieulist[-len(adieulist):-1] # creates a list without the last entree
    comma = ", ".join(comma) # makes a string out of the "comma" list
    return comma

if __name__ == "__main__":
    main()
