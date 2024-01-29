# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")
print ("erste",CamelCase)
# print (snake)

for upperLetter in CamelCase:
        Camelcase = ""
        print ("zweite",CamelCase)
        if upperLetter.isupper():
            # "+=" adds another variable to the previous one.
            CamelCase += " " + upperLetter
            print ("dritte",CamelCase)
        else:
            CamelCase += upperLetter
            print ("vierte",CamelCase)

