einkaufsliste = {}
alphalist = []
letter = {}
while True:
    try:
        var = input()
        if einkaufsliste.get(var) == None:
            einkaufsliste[var] = 1
        else:
            einkaufsliste[var] = einkaufsliste.get(var) + 1
        alphalist = sorted(einkaufsliste, key=None)
        print(alphalist)
        letter = letter.

    except EOFError:
        for k,v in einkaufsliste.items():
            print(v,k.upper())
        exit()



