from seasons import time_delta
from seasons import number_to_word
import pytest


def main():
    test_time_delta()
    test_number_to_word()


def test_time_delta():
    #with pytest.raises(ValueError):
    #    time_delta("2024.01.04")
    assert time_delta("2024.01.04") == "Invalid date"


def test_number_to_word():
    assert number_to_word(1) == "one"


if __name__ == "__main__":
    main()

