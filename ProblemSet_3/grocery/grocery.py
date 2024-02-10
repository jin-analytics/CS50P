
einkaufsliste = {}
while True:
    try:
        var = input()
        if einkaufsliste.get(var) == None:
            einkaufsliste[var] = 1
            print(einkaufsliste)
        else:
            einkaufsliste[var] = einkaufsliste.get(var) + 1
            print(einkaufsliste)

        for k,v in einkaufsliste.items():
            print(v,k.capitalize())

    except EOFError:
        exit()



