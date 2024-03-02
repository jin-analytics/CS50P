from plates import

def main():
    test_letter_size()

def test_letter_size():
    assert is_valid("CS") == True
    assert is_valid("CSCSCS") == True
    assert is_valid("C") == False
    assert is_valid("CSCSCSC") == False


if __name__ == "__main__":
    main()
