#from numb3rs import validate
import pytest

from numb3rs_wrong import validate

def main():
    test_number_format_in_dot_decimal()
    test_number_under_256()


#______________________________________________________
def test_number_format_in_dot_decimal():
    ip_list = [
        'cat',
        'cat.dog.mouse.bird',
        '1.2.34',
        '1.cat.dog',
        '1.2.3.4.5',
        '1,2,3,4',
        ]

    #with pytest.raises(SystemExit):
    for entrees in ip_list:
        assert validate(entrees) == False

#______________________________________________________
def test_number_under_256():
    ip_list = [
        '256.0.0.0',
        '0.256.0.0',
        '0.0.256.0',
        '0.0.0.256',
        ]
    for entrees in ip_list:
        assert validate(entrees) == False


if __name__ == "__main__":
    main()
