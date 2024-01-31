def main():
    # This Program changes the CamelCase input to Snake_Case input
    cc = input ("camelCase: ")
    #print ("erste",CamelCase)
    sc = snake_case(cc)
    print(sc)

def snake_case(CamelCase):
    for upperLetter in CamelCase:
        if upperLetter.isupper():
            # finds in each loop upperletter in string and adds a "_" to it
            # if 5 upperletter, then 5 iterations
            CamelCase = CamelCase.replace(str(upperLetter), "_" + str(upperLetter))
    # lowers all upperletters
    CamelCase = CamelCase.lower()
    # returns CamelCase to main(), which then will be called "sc" for snakecase
    return CamelCase

if __name__ == "__main__":
    main()
