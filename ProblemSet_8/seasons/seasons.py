from datetime import date
from datetime import timedelta
import datetime
import inflect



def main():
    delta = time_delta(input("Date of Birth: ")) #format YYYY-MM-DD
    ...


def time_delta(birthday):
    birthday = birthday.split('-')
    birthday = datetime.date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
    passed_days = date.today() - birthday
    return passed_days.days

def number_to_word():
    ...
    #p = inflect.engine()
    #words = p.number_to_words(1111)
    #print(words)



if __name__ == "__main__":
    main()
