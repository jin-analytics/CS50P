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
    test_x_and_y_is_a_int()

def test_x_and_y_is_a_int():
    f1 = ("1/2").split("/")
    f2 = ("a/2").split("/")
    f3 = ("1/b").split("/")
    assert convert(f1) == 50
    assert convert(f2) == False
    assert convert(f3) == False

#def test_returned_fraction_is_percentage():
  #  assert convert("1/2") == 50
 #   assert convert("3/2") == False
   # assert convert("1/b") == False
##
#def test_x_and_y_is_a_str():
 #   assert convert("1/2") == 50
 #   assert convert("a/2") == False
 #   assert convert("1/b") == False

def test_dont_divide_by_zero():
    ...

if __name__ == "__main__":
    main()
