from twttr import shorten

def main():
    tweet = input("Input: ")
    #print("Output:", shorten(tweet))
    test_lower(tweet)

# compare the selected vowes with the one removed
def test_lower(tw):
   shortened_word = shorten(tw)
   print(shortened_word)
   for letters in shortened_word:
       print(letters)
       assert letters != "a" and "e" and "i" and "o" and "u"


#def test_upper():


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

