from twttr import shorten

def main():
    tweet = input("Input: ")
    #print("Output:", shorten(tweet))
    test_lower(tweet)
    test_upper(tweet)

# compare the selected vowes with the one removed
def test_lower(tw):
   shortened_word = shorten(tw)
   for letters in shortened_word:
      try:
        vowelslist = ["a","e","i","o","u"]
        for vowels in vowelslist:
            assert letters != vowels
      except AssertionError:
         print("Still some vowels left... ->", vowels)

def test_upper(tw):
    shortened_word = shorten(tw)
    for letters in shortened_word:
      try:
        vowelslist = ["A","E","I","O","U"]
        for vowels in vowelslist:
            assert letters != vowels
      except AssertionError:
         print("Still some vowels left... ->", vowels)


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

