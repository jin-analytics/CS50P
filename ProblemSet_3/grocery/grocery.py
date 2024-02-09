####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():
    # Empty dictionary
    shopping_list = {}

    while True:
        try:
            shopping_list[input()]
            for i in shopping_list:
                print(shopping_list)
                if item == shopping_list.get(i):
                    shopping_list[i] = shopping_list.get(i) + 1
                    print(shopping_list)
                else:
                    shopping_list[i] = 1
                    print(shopping_list)




        except EOFError:
            for entrees in shopping_list:
                print(shopping_list.key(entrees), shopping_list.value(entrees))




main()
