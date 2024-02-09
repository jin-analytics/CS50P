def main():

    list = []

    while True:
        try:
            item = input()
            list.append(item)
            print(list)
        except EOFError:
            print("new",list[0])



#def add_item_to_list(i):
#    new_list = i
#   return new_list

main()
