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

        # sorts alphabeticaly
        #alphalist = sorted(einkaufsliste)
        #print(alphalist)
        #for i in alphalist:




    except EOFError:
        einkaufsliste = {}
        einkaufsliste = sorted(einkaufsliste)
        for k,v in einkaufsliste.items():
            print(v,k.upper())
        exit()



