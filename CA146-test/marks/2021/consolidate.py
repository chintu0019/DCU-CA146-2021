
import sys
marks = {}

n = 9

import math

for line in sys.stdin.readlines():
   [user, mark] = line.split()[:2]
   if user not in marks:
      marks[user] = 0
   marks[user] += float(mark)

for user in marks:
   print user, int(round(marks[user] / 3))
