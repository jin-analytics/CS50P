# This Program changes the CamelCase input to Snake_Case input
CamelCase = input ("camelCase: ")
splitAtUpperCase(CamelCase)
# print (snake)

def splitAtUpperCase(text):
    result = ""
    for char in text:
        if char.isupper():
            result += " " + char
        else:
            result += char
            print (result)
    return result.split()
