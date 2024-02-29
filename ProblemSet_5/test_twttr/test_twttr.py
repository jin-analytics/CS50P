from twttr import shorten

# compare the selected vowes with the one removed
def test_lowercase_vowels(): #a,e,i,o,u
    tweet = ("twitter") # Output should be: "twttr"
    assert shorten(tweet) == "twttr"

def test_lowercase_vowels_and_sentences(): #a,e,i,o,u
    tweet = ("twitter and ouchie") # Output should be: "twttr nd ch"
    assert shorten(tweet) == "twttr nd ch"

def test_numbers_spaces_and_signs(): #1,2,3,4,5,6,7,8,9
    tweet = ("combo 1-2-3, left 4,5,6 & 7 8 9") # Output should be: "cmb  lft     "
    assert shorten(tweet) == "cmb  lft     "
