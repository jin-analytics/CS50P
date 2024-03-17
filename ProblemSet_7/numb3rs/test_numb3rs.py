from numb3rs import validate
import pytest

#def main():
#    test_number_format_in_dot_decimal()
#   test_number_between_0_and_255()


#______________________________________________________
def test_number_format_in_dot_decimal():
    ip_list = [
        'cat',
        'cat.dog.mouse.bird',
        '1.2.34',
        '1.23.4',
        '12.3.4',
        '1,2,3,4',
        ]

    with pytest.raises(SystemExit):
        for entrees in ip_list:
            assert validate(entrees) == False

#______________________________________________________
def test_number_between_0_and_255():
    ip_list = [
        '256.0.0.0',
        '0.256.0.0',
        '0.0.256.0',
        '0.0.0.256',
        '-1,0,0,0',
        '0,-1,0,0',
        '0,0,-1,0',
        '0,0,0,-1',
        ]

    with pytest.raises(SystemExit):
        for entrees in ip_list:
            assert validate(entrees) == False


#if __name__ == "__main__":
#    main()
