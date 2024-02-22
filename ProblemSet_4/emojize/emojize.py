import emoji
import re

#x = "This is a sentence. (once a day) [twice a day]"
#re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", x)

def main():
    emo = input("Input: ")
    #line_check(emo)
    #print(emoji.emojize(f"Output: {emo}", language='alias'))

    #re.sub("::", "", emo)
    #emoji_selected = emo.split(':', maxsplit = 1)
    print(re.sub("::", "", emo))

#__________________________________________________
# Checks if ther is a _ inside the string "emo"
def line_check(e):

    for i in e:
        if i == "_":
            print(emoji.emojize(f"Output: {e}"))


main()
