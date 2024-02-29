from twttr import shorten

# compare the selected vowes with the one removed
def test_lower():
   shortened_word = shorten()
   print(shortened_word)
   for letters in shortened_word:
      vowelslist = ["a","e","i","o","u"]
      for vowels in vowelslist:
          assert letters != vowels

def test_upper():
    shortened_word = shorten()
    for letters in shortened_word:
        vowelslist = ["A","E","I","O","U"]
        for vowels in vowelslist:
            assert letters != vowels
