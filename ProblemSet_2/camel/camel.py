# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")
splitAtUpperCase(result)
 print (result)

def splitAtUpperCase(CamelCase):
    result = ""
    for char in CamelCase:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result.split()
