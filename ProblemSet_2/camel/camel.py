# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")
#snake=splitAtUpperCase()
# print (snake)

def splitAtUpperCase(CamelCase):
    result = ""
    for char in CamelCase:
        if char.isupper():
            result += " " + char
        else:
            result += char
            print (result)
    return result.split()
