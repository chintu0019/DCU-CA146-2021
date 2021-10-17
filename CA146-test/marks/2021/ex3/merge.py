
import sys

marks = {}

for line in sys.stdin.readlines():
   toks = line.split()
   user = toks[0]
   mark = int(toks[1])
   if user not in marks:
      marks[user] = 0
   marks[user] += mark

for user in marks:
   print user, marks[user]
