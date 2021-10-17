
import sys
from random import randint

months = "0 31 28 31 30 31 30 31 31 30 31 30 31".split()
months = map(int, months)

# for line in sys.stdin.readlines():
for line in range(3):
    month = randint(1, 12)
    day = randint(1, months[month])
    year = randint(1950, 2017)
    print "{}/{}/{}".format(day, month, year)
