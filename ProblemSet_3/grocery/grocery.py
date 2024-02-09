def main():
    while True:
        item = input()
        list = add_item_to_list(item)
        list = list + list
        print(list)


def add_item_to_list(i):
    new_list = i
    return new_list

main()
