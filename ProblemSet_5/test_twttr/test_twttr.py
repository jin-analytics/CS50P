from twttr import shorten

# compare the selected vowes with the one removed
def test_lowercase_vowels(): #a,e,i,o,u
    tweet = ("twitter and ouchie") # Output should be: "twttr nd ch"
    assert shorten(tweet) == "twttr nd ch"
