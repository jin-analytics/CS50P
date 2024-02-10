
einkaufsliste = {} #creates empty dictionary which will be filled in the while loop

while True:
    try:
        var = input() #creates variable where user inputs grocerie products
        #if the product doesnt exist in the "einkaufsliste", then product gets value 1
        #else the value of the product gets increased by 1
        if einkaufsliste.get(var) == None:
            einkaufsliste[var] = 1
        else:
            einkaufsliste[var] = einkaufsliste.get(var) + 1

    except EOFError:
        # sorts the keys from dict(einkaufsliste) alphabetically
        #einkaufsliste = dict(sorted(einkaufsliste.items()))
        einkaufsliste = sorted(einkaufsliste.items())
        for k,v in einkaufsliste.items():
            # changes value and key position and capitalizes all letters
            print(v,k.upper())
        exit()



