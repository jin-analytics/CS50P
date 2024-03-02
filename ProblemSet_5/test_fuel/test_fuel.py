from fuel import convert
from fuel import gauge
import pytest

#_________convert
# input "x/y" is an string
# x is integer and y is integer
# returned fraction is precentage and rounded to the nearest int between 0 and 100
# if x or y is not int then raise ValueError
# if x is greater than y then raise an ValueError
# if y is 0 than raise an ZeroDivisionError

#_________gauge
# expects an int and returns a str
# "E" if int is less/equal 1
# "F" if in is greater/equal 99
# "z%" otherwise, wherein z is the same int

def main():
    test_x_and_y_at_convert()
    test_if_gauge_outputs_percent()
    test_if_0_raise_error()
    test_if_0_value_error()
    test_if_E_comes()
    test_if_F_comes()


def test_x_and_y_at_convert():
    assert convert("2/3") == 67

def test_if_gauge_outputs_percent():
    assert gauge(67) == "67%"

def test_if_0_raise_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_if_0_value_error():
    with pytest.raises(ValueError):
        convert("bunny/hop")

def test_if_E_comes():
    assert gauge(1) == "E"
    assert gauge(2) != "E"

def test_if_F_comes():
    assert gauge(99) == "F"
    assert gauge(50) != "F"


if __name__ == "__main__":
    main()
