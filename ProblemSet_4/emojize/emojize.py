





#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
#print(emoji.emojize('Python is :thumbs_up:'))


def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__":
    main()
