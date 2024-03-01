from plates import is_valid
from plates import length
import pytest

@pytest.fixture
def testplate():
    testplate("CS50")
    return testplate


def test_if_the_length_is_between_2_and_6():
    assert length(testplate) == True
