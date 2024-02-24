adieulist = []


def main():
    while True:

        try:
            n = input("Name: ") #creates variable where the name gets added to the list "adieulist"
            adieulist.append(n)
            #print(adieulist)

        except EOFError:
            if len(adieulist) == 1:
                #print(len(adieulist))
                print(f"Adieu, adieu, to {adieulist[-len(adieulist)]}") #first entree of somelist[-len(somelist)]

            elif len(adieulist) == 2:
                #print(len(adieulist))
                print(f"Adieu, adieu, to {adieulist[-len(adieulist)]} and {adieulist[-n]}") #last entree of somelist[-n]
            elif len(adieulist) > 2:
                #print(len(adieulist))
                print(f"Adieu, adieu, to {name_string(adieulist)} and {adieulist[-n]}")


            exit()

# creates a string of all names (except the last one), wihich will all be seperated
# by a comma and then returns the single string of these names
def name_string(adieulist):
    comma = adieulist[-len(adieulist):-1] # creates a list without the last entree
    comma = ", ".join(comma) # makes a string out of the "comma" list
    return comma


if __name__ == "__main__":
    main()
