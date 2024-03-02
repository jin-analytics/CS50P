from plates import is_valid

def main():
    test_letter_size()
    #test_if_there_are_2_letter()
    #test_if_there_is_no_zero_at_beginning_of_numberblock()
    #test_if_numberblock_has_no_letter_in_it()
    #test_if_there_is_no_sign_or_space()

# test if length smaller 2 or bigger 6 returns false
def test_letter_size():
    assert is_valid("CS") == True
    assert is_valid("CSCSCS") == True
    assert is_valid("C") == False
    assert is_valid("CSCSCSC") == False

# test if letter block is atleast 2 chars
def test_if_there_are_2_letter():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False

# test if number block has no zero at beginning
def test_if_there_is_no_zero_at_beginning_of_numberblock():
    assert is_valid("CS50"): True
    assert is_valid("CS05"): False

# test if number block has no letter in it
def test_if_numberblock_has_no_letter_in_it():
    assert is_valid("CS50") == True
    assert is_valid("CS50C") == False

# test if no spaces or signs get detected
def test_if_there_is_no_sign_or_space():
    assert is_valid("CS#50") == False
    assert is_valid("CS 50") == False




if __name__ == "__main__":
    main()
