# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")

# print (snake)

for char in CamelCase:
        if char.isupper():
            # "+=" adds another variable to the previous one.
            # Example:
            # x = 5
            # x += 2
            # X is now 7 ...
            result += " " + char
          #  print ("if",result)
        else:
            result += char
           # print ("else",result)

print(result)
