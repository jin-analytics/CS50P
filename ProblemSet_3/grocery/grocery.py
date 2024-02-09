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
        #        list.update({new_key: new_value + 1})
                # Add a key-value pair to empty dictionary in python
            shopping_list.update({new_key: new_value})
            print(shopping_list)
        except EOFError:
            for entrees in shopping_list:
                print(shopping_list.key(entrees), shopping_list.value(entrees))

def count_items(i):
    for i in shopping_list:
        if i == shopping_list.key(i):
            shopping_list.value(i) = shopping_list-value(i) + 1



main()
