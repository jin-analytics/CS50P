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

test_dont_divide_by_zero()

def test_dont_divide_by_zero():
    with pytest raises.ZeroDivisionError:
    100/0
    #assert convert("100/0") raise ZeroDivisionError





if __name__ == "__main__":
    main()
