# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")

# print (snake)

for char in CamelCase:
        if char.isupper():
            result += " " + char
          #  print ("if",result)
        else:
            result += char
           # print ("else",result)

print(result)
