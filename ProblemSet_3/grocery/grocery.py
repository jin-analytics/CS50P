####### try to do this solution:
#1 create a dictionary with inputs
#2 associate a number to each input
#3 if the same input occurs, add +1 to count the entrees



def main():

    value = 1
    list = {}

    while True:
        try:
            item = input()
            list.append(item)
            print(list)

        except EOFError:
            #for entrees in list:
            #   print(list(entrees))
            print(list)
            break



#def add_item_to_list(i):
#    new_list = i
#   return new_list

main()
