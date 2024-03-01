from plates import is_valid

def test_input_is_not_str():
    assert is_valid(1) == False
#def test_length_between_2_and_6():
