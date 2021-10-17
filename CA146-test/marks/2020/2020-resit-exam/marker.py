import sys

marks = {}

for line in sys.stdin:
   mark = line.split()[1]
   user = line.split("/")[1]
   if user not in marks:
      marks[user] = 0
   marks[user] += int(mark)

for user in marks:
   print user, marks[user]
