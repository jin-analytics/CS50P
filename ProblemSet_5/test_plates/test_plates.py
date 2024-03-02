from plates import is_valid

def main():
    test_letter_size()

# test if length smaller 2 or bigger 6 returns false
def test_letter_size():
    assert is_valid("CS") == True
    assert is_valid("CSCSCS") == True
    assert is_valid("C") == False
    assert is_valid("CSCSCSC") == False

# test if letter block is atleast 2 chars

# test if number block has no zero at beginning

# test if number block has no letter in it






if __name__ == "__main__":
    main()
