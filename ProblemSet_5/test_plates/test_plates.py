from plates import is_valid

def test_input_is_not_str():
    s = ("1")
    assert is_valid(s) == False
#def test_length_between_2_and_6():
