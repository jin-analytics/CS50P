from plates import is_valid, length, sign_detection, letterblock_atleast_two_char, numberblock_only_number, splitter, first_number_zero
#from plates import length
#from plates import sign_detection
#from plates import letterblock_atleast_two_char
#from plates import numberblock_only_number
#from plates import splitter
#from plates import first_number_zero
import pytest

@pytest.fixture
def plate():
    return ("CS50")
    #return ("")



def test_length(plate):
    assert length(plate) == True

def test_sign_detection(plate):
    assert sign_detection(plate) == None

def test_if_letterblock_has_atleast_two_chars(plate):
    if splitter(plate) == None:
        pass
    else:
        assert letterblock_atleast_two_char(splitter(plate)) == True

def test_if_numberblock_has_only_numbers(plate):
    if splitter(plate) == None:
        pass
    else:
        assert numberblock_only_number(splitter(plate)) == True

def test_if_the_first_number_is_zero(plate):
    if splitter(plate) == None:
        pass
    else:
        assert first_number_zero(splitter(plate)) != False

def test_if_is_valid_func_gives_True(plate):
    assert is_valid(plate) == True
