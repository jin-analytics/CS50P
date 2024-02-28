from twttr import shorten

def main():
    #tweet = str("1234567890!§$%&/=twitter")
    #tweet = input("Input: ")
    test_lower()
    test_upper()
    test_numbers()
    test_signs()

# compare the selected vowes with the one removed
def test_lower():
   shortened_word = shorten()
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
    shortened_word = shorten()
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
    input = shorten()
    for number in input:
        assert number.isdigit() != True

def test_signs():
    input = shorten()
    for signs in input:
        assert signs.isalpha() == True


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

