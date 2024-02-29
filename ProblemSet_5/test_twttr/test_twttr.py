from twttr import shorten

# compare the selected vowes with the one removed
def test_lowercase_vowels(): #a,e,i,o,u
    word = ("twitter") # Output should be: "twttr"
    assert shorten(word) == "twttr"

def test_uppercase_vowels(): #A,E,I,O,U
    word = ("TWITTER") # Output should be: "twttr"
    assert shorten(word) == "twttr"

#def test_lowercase_and_vowels_and_sentences(): #a,e,i,o,u
#    word = ("twitter and ouchie") # Output should be: "twttr nd ch"
#    assert shorten(word) == "twttr nd ch"
#    word = ("TWITTER AND OUCHIE") # Output should be: "twttr nd ch"
#    assert shorten(word) == "TWTTR ND CH"

#def test_numbers_spaces_and_signs(): #1,2,3,4,5,6,7,8,9
#    word = ("combo 1-2-3, left 4,5,6 & 7 8 9") # Output should be: "cmb  lft     "
#    assert shorten(word) == "cmb  lft     "
