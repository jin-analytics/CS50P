import emoji
#print(emoji.emojize('Python is :thumbs_up:'))
#print(emoji.emojize('Python is :thumbsup:', language='alias'))


emo = input("Input: ")

for i in emo:
    #print(i)
    if i == "_":
        print(emoji.emojize(f"Output: {emo}"))

print(emoji.emojize(f'Output: {emo}'))
