from seasons import time_delta
from seasons import number_to_word
from datetime import date
import pytest


def main():
    test_time_delta()
    test_number_to_word()

def test_time_delta():
    today = str(date.today())
    assert time_delta(today) == 0

def test_number_to_word():
    assert number_to_word(1) == "one"

def test_ValueError():
    with pytest.raises(SystemExit):
        time_delta("26.12.1994")

if __name__ == "__main__":
    main()

