def name_string(adieulist):
    comma = adieulist[-len(adieulist):-1] # creates a list without the last entree
    comma = ", ".join(comma) # makes a string out of the "comma" list
    return comma
