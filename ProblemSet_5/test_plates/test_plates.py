from plates import is_valid

def test_if_the_length_is_between_2_and_6():
    plate = ("CS50")
    assert len(is_valid(plate)) == 4
