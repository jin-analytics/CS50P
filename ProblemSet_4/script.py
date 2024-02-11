#import random
from random import shuffle

for i in range(3):
    #coin = random.choice(["heads","tails"])
    #coin = choice(["heads","tails"])
    cards = ["jack","queen","king"]
    shuffle(cards)
    for card in cards:
        print(card)

    #print(coin)
