from numb3rs import validate
import pytest

def main():
    test_format_in_dot_decimal()

def test_format_in_dot_decimal():
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
            validate(entrees)


if __name__ == "__main__":
    main()
