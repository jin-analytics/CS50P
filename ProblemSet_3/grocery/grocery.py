
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

        for k,v in einkaufsliste:
            print(k,v)

    except EOFError:
        exit()



