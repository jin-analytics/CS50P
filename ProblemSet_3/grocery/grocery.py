####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():
    # Empty dictionary
    list = {}
    new_value = 1

    while True:
        try:
            new_key = input()
        #        list.update({new_key: new_value + 1})
                # Add a key-value pair to empty dictionary in python
            list.update({new_key: new_value})
            print(list)
        except EOFError:
            for entrees in list:
                print(list.key(entrees), list.value(entrees))

def count_items(i):
    for i in list:
        if i == list.key(i):
            list.value(i) = list-value(i) + 1



main()
