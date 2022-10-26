from random import randint
from datetime import date

year = randint(1600, 2023)
month = randint(1, 12)
day = randint(1, 30)
print("Random date:", date(year, month, day))
