
def main():
    # Empty dictionary
    shopping_list = {}

    while True:
        try:
            shopping_list = input()
            # sets the default value "v" +1
            #shopping_list.setdefault(input()[,v + 1])
            print(shopping_list)

        except EOFError:
           exit()




main()
