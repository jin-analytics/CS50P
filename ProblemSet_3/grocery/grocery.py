####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():
    # Empty dictionary
    shopping_list = {}
    new_value = 1

    while True:
        try:
            new_key = input()
            print("0",shopping_list)

            for i in shopping_list:
                shopping_list = shopping_list{new_key:new_value})
                if i == shopping_list.get(i):
                    shopping_list[i] = shopping_list.get(i) +1
                    print("1",shopping_list)
                    print("2",shopping_list[1])
            #shopping_list = shopping_list.update({new_key:new_value})
            #print("3",shopping_list)



        except EOFError:
            for entrees in shopping_list:
                print(shopping_list.key(entrees), shopping_list.value(entrees))




main()
