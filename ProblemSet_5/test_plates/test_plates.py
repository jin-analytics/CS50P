from plates import is_valid
from plates import length
from plates import sign_detection
from plates import letterblock_atleast_two_char
from plates import numberblock_only_number
from plates import splitter
import pytest

@pytest.fixture
def plate():
    return ("CS50")
    #return ("")


def test_if_the_length_is_between_2_and_6(plate):
    assert length(plate) == True

def test_if_signs_or_spaces_get_detected(plate):
    assert sign_detection(plate) == None

def test_if_letterblock_has_atleast_two_chars(plate):
    plate_split = splitter(plate)
    assert letterblock_atleast_two_char(plate_split) == True

def test_if_numberblock_has_only_numbers(plate):
    plate_split = splitter(plate)
    assert numberblock_only_number(plate_split) == True
