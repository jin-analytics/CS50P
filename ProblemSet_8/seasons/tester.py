from datetime import date
from datetime import timedelta
import inflect
import datetime



birthday = input()
birthday = birthday.split('-')
birthday = datetime.date(int(birthday[0]), int(birthday[1]), int(birthday[2]))

date = date.today() - birthday
print(date.tseconds())
