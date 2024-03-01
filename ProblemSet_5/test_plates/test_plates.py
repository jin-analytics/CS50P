from plates import is_valid
from plates import length
from plates import sign_detection
from plates import letterblock_atleast_two_char
from plates import numberblock_only_number
from plates import splitter
from plates import first_number_zero
from plates import main
import pytest

def main():
    @pytest.fixture
    def plate():
        return ("CS50")
        #return ("")



    def test_length(plate):
        assert length(plate) == True

    def test_sign_detection(plate):
        assert sign_detection(plate) == None

#def test_if_letterblock_has_atleast_two_chars():
    #plate_split = splitter()
    #assert letterblock_atleast_two_char(plate_split) == True

#def test_if_numberblock_has_only_numbers():
 #   plate_split = splitter()
 #   assert numberblock_only_number(plate_split) == True

#def test_if_the_first_number_is_zero():
 #   plate_split = splitter()
  #  assert first_number_zero(plate_split) == True
if __name__ == "__main__":
    main()
