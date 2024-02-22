import emoji

emo = input("Input: ")

for i in emo:
    #print(i)
    if i == "_":
        print(emoji.emojize(f"Output: {emo}"))

print(emoji.emojize(f"Output: {emo}", language='alias'))
