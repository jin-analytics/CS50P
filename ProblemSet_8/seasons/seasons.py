from datetime import date
from datetime import timedelta
import datetime
import inflect



def main():
    delta = time_delta(input("Date of Birth: ")) #format YYYY-MM-DD
    print(number_to_word(delta))


def time_delta(birthday):
    birthday = birthday.split('-')
    birthday = datetime.date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
    passed_days = date.today() - birthday
    return passed_days.days

def number_to_word(d):
    p = inflect.engine()
    return p.number_to_words(d)




if __name__ == "__main__":
    main()
