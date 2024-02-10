


einkaufsliste = {}
while True:
    var = input()
    for k in einkaufsliste:
        if k == var:
            einkaufsliste[var] = 2
            print(einkaufsliste)
        else:
            einkaufsliste[var] = 1
            print(einkaufsliste)




