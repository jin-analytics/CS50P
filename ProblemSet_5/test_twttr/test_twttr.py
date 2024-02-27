from twttr import shorten
import pytest

def main():
    test_lower()
    test_upper()

# compare the selected vowes with the one removed
def test_lower():
   shortened_word = shorten("twitter")
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

def test_upper():
    shortened_word = shorten("twitter")
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

# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

