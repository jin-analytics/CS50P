from twttr import shorten

def main():
    test_lower()
    test_upper()
    test_numbers()
    test_signs()

# compare the selected vowes with the one removed
def test_lower(word):
   shortened_word = shorten(word)
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
    shortened_word = shorten("A E I O U")
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

def test_numbers():
    input = shorten("1234567890")
    for number in input:
        assert number.isdigit() != True

def test_signs():
    input = shorten(" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
    for signs in input:
        assert signs.isalpha() == True


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

