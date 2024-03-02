from twttr import shorten

def main():
    test_if_lower_vowels_gets_replaced()

def test_if_lower_vowels_gets_replaced():
    assert shorten("twitteraeiou") == "twttr"

def test_if_lower_vowels_gets_replaced():
    assert shorten("TWITTERAEIOU") == "TWTTR"

def test_if_numbers_dont_get_changed():
    assert shorten("1234567890") == "1234567890"

def test_if_spaces_dont_get_changed():
    assert shorten("twitter   ") == "twttr   "


if __name__ == "__main__":
    main()
