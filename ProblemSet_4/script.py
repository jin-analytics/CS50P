#import random
#import statistics
import sys

#for i in range(3):
    #coin = random.choice(["heads","tails"])
    #coin = choice(["heads","tails"])
    #cards = ["jack","queen","king"]
    #shuffle(cards)
    #for card in cards:
    #   print(card)
    #print(coin)

#grade = statistics.mean([100, 90])
#print(grade)


#print(sys.argv[0])

if len(sys.argv) <2:
    sys.exist("too few")

for arg in sys.argv[1:]:
    print("hello", arg)
