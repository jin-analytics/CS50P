from datetime import date
from datetime import timedelta
import inflect



birthday = input()

date = date.today() - birthday
print(date)
