def main():
    # This Program changes the CamelCase input to Snake_Case input
    cc = input ("camelCase: ")
    #print ("erste",CamelCase)
    cc = snake_case(cc)
    #print(cc)
    #print(snake_case(cc))

def snake_case(CamelCase):
    for upperLetter in CamelCase:
        if upperLetter.isupper():
            # finds upperletter in string and adds a "_" to it
            CamelCase = CamelCase.replace(str(upperLetter), "_" + str(upperLetter))
            CamelCase = CamelCase.lower()
            print ("->", CamelCase)
            # breaks the for loop, otherwise there are n iterations for the number of upperletters
            break
        else:
            break
    return CamelCase

if __name__ == "__main__":
    main()
