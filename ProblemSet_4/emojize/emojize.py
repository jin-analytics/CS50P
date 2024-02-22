import emoji

def main():
    emo = input("Input: ")
    line_check(emo)
    print(emoji.emojize(f"Output: {emo}", language='alias'))



#__________________________________________________
# Checks if ther is a _ inside the string "emo"
def line_check(e):

    for i in e:
        if i == "_":
            print(emoji.emojize(f"Output: {e}"))


main()
