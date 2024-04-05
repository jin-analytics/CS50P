from datetime import date
import sys
import datetime
import inflect
import re


def main():
    # = time_delta(input("Date of Birth: ")) #format YYYY-MM-DD
    delta = input("Date of Birth: ")
    delta = time_delta(delta)
    print(remove_and(number_to_word(delta)).capitalize() + " minutes")

def time_delta(birthday):
    try:
        birthday = birthday.split('-')
        birthday = datetime.date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
        passed_days = date.today() - birthday
        passed_minutes = int(passed_days.days)*24*60
        return passed_minutes
    except ValueError:
        sys.exit("Invalid date")

def number_to_word(d):
    p = inflect.engine()
    return p.number_to_words(d)

def remove_and(d):
    return re.sub(' and ',' ', d)


if __name__ == "__main__":
    main()
