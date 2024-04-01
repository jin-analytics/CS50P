from datetime import date
from datetime import timedelta
import inflect



birthday = input()
birthday = birthday.split('-')
birthday = datetime.date(birthday[0], birthday[1], birthday[2])

date = date.today() - birthday
print(date)
