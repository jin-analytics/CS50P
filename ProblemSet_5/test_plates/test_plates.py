from plates import is_valid
from plates import length
import pytest

@pytest.fixture
def plate():
    return ("CS50")
    #return ("")


def test_if_the_length_is_between_2_and_6(plate):
    assert length(plate) == True
