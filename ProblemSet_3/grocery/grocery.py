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
        einkaufsliste = {sorted(einkaufsliste.keys():values())}
        # sorts alphabeticaly
        #alphalist = sorted(einkaufsliste)
        print(einkaufsliste)
        #for i in alphalist:




    except EOFError:
        #einkaufsliste = {}
        einkaufsliste = sorted(einkaufsliste.values())
        for k,v in einkaufsliste.items():
            print(v,k.upper())
        exit()



