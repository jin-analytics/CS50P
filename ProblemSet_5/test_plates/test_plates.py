from plates import is_valid
from plates import length
from plates import sign_detection
from plates import letterblock_atleast_two_char
from plates import numberblock_only_number
from plates import splitter
from plates import first_number_zero
from plates import main
import pytest

@pytest.fixture
def plate():
    return ("NRVOUS")
    #return ("")



def test_length(plate):
    assert length(plate) == True
def test_sign_detection(plate):
    assert sign_detection(plate) == None

def test_if_letterblock_has_atleast_two_chars(plate):
    plate_split = splitter(plate)
    if letterblock_atleast_two_char(plate_split) == None:
        pass
    else:
        assert letterblock_atleast_two_char(plate_split) == True

def test_if_numberblock_has_only_numbers(plate):
    plate_split = splitter(plate)
    if numberblock_only_number(plate_split) == None:
        pass
    else:
        assert numberblock_only_number(plate_split) == True

def test_if_the_first_number_is_zero(plate):
    plate_split = splitter(plate)
    assert first_number_zero(plate_split) != False

