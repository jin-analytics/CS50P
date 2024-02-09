####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():
    # Empty dictionary
    list = {}
    while True:

        new_key = input()
        new_value = 1

        # Add a key-value pair to empty dictionary in python
        list.update({new_key: new_value})

        print(list)

main()
