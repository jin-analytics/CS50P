from plates import is_valid
from plates import length

@pytest.fixture
def plate():
    plate("CS50")


def test_if_the_length_is_between_2_and_6():
    plate = (input)
    assert length(plate) == True
