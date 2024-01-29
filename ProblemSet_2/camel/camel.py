# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")
print ("erste",CamelCase)
# print (snake)

for char in CamelCase:
        Camelcase = ""
        print ("zweite",CamelCase)
        if char.isupper():
            # "+=" adds another variable to the previous one.
            CamelCase += " " + char
            print ("dritte",CamelCase)
        else:
            CamelCase += char
            print ("vierte",CamelCase)

