


einkaufsliste = {}
while True:
    var = input()
    einkaufsliste[var] = 1
    for key in einkaufsliste:
        if key == var:
            print("got ya",key)
        else:
            einkaufsliste[var] = 1
    print(einkaufsliste)




