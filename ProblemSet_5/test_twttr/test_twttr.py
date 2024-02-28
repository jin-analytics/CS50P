from twttr import shorten

def main():
    #tweet = input("Input: ")
    test_lower(tweet)
    test_upper(tweet)
    test_numbers(tweet)
    test_signs(tweet)

# compare the selected vowes with the one removed
def test_lower(t):
   shortened_word = shorten(t)
   print(shortened_word)
   for letters in shortened_word:
      vowelslist = ["a","e","i","o","u"]
      for vowels in vowelslist:
          assert letters != vowels
#      try:
#        vowelslist = ["a","e","i","o","u"]
#        for vowels in vowelslist:
#            assert letters != vowels
#      except AssertionError:
#         print("Still some vowels left... ->", vowels)

def test_upper(t):
    shortened_word = shorten(t)
    for letters in shortened_word:
        vowelslist = ["A","E","I","O","U"]
        for vowels in vowelslist:
            assert letters != vowels
#      try:
#        vowelslist = ["A","E","I","O","U"]
#        for vowels in vowelslist:
#            assert letters != vowels
#      except AssertionError:
#         print("Still some vowels left... ->", vowels)

def test_numbers(t):
    input = shorten(t)
    for number in input:
        assert number.isdigit() != True

def test_signs(t):
    input = shorten(t)
    for signs in input:
        assert signs.isalpha() == True


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

