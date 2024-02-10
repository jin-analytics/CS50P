
def main():
    # Empty dictionary
    shopping_list = {}

    while True:
        try:
            shopping_list = shopping_list.update(input())
            print(shopping_list)
        except EOFError:
           exit()




main()
