from plates import is_valid
from plates import length
from plates import sign_detection
from plates import letterblock_atleast_two_char
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

    assert letterblock_atleast_two_char(splitter(plate)) == True
