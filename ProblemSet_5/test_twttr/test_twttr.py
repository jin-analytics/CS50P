from twttr import shorten

def main():
    tweet = input("Input: ")
    #print("Output:", shorten(tweet))
    test_lower(tweet)

# compare the selected vowes with the one removed
def test_lower(tw):
   shortened_word = shorten(tw)
   for letters in shortened_word:
      try:
        vowelslist = ["a","e","i","o","u"]
        print(vowelslist[0])
        for i in vowelslist:
            print(i)
            assert letters != vowelslist[i]
            print(vowelslist[i])
      except AssertionError:
         print("Still some vowels left!")



#def test_upper():


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

