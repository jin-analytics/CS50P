####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():
    # Empty dictionary
    shopping_list = {}

    while True:
        try:
            shopping_list: dict = input()
            # sets the default value "v" +1
            #shopping_list.setdefault(input()[,v + 1])
            print(shopping_list)

        except EOFError:
           exit()




main()
