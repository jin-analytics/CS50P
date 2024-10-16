from working import convert
import pytest

def main():
    test_ante_end_post_meridiem()
  #  test_invalid_minutes_in_time()
  #  test_invalid_input()

# check if is possible to start at any timeframe the day/night
def test_ante_end_post_meridiem():
    meridiem = ['5:00 PM to 9:00 AM', '5:00 AM to 9:00 PM']
    assert convert(meridiem[0]) == "17:00 to 09:00"
    assert convert(meridiem[1]) == "05:00 to 21:00"

# check if invalid minute input gets detected
def test_invalid_minutes_in_time():
    meridiem = ['5:60 PM to 9:00 AM', '5:00 AM to 9:60 PM']
    with pytest.raises(ValueError):
        convert(meridiem[0])
        convert(meridiem[1])


# check if invalid input gets detected...
# correct input: "hh:mm AM/PM to hh:mm AM/PM" or "hh AM/PM to hh AM/PM"
def test_invalid_input():
    meridiem = ['5:00 PM - 9:00 AM', '5:00 AM']
    with pytest.raises(ValueError):
        convert(meridiem[0])
        convert(meridiem[1])


if __name__ == "__main__":
    main()
