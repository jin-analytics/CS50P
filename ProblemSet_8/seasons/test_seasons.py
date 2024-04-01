from seasons import time_delta
from seasons import number_to_word

def main():
    test_time_delta()
    test_number_to_word()


def test_time_delta():
    assert test_time_delta("2024.01.04") == "Invalid date"


def test_number_to_word():
    assert test_time_delta("2024.01.04") == "Invalid date"


if __name__ == "__main__":
    main()

