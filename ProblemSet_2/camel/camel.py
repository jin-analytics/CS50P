# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")

# print (snake)

for char in CamelCase:
        result=""
        if char.isupper():
            result += " " + char
        else:
            result += char
            print (result)
            
print (result)
