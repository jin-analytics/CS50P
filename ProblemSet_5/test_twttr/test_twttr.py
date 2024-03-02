from twttr import shorten

def main():
    test_if_lower_vowels_gets_replaced()

def test_if_lower_vowels_gets_replaced():
    assert shorten("twitteraeiou") == "twttr"

def test_if_lower_vowels_gets_replaced():
    assert shorten("TWITTERAEIOU") == "TWTTR"

if __name__ == "__main__":
    main()
