
import sys
marks = {}

for line in sys.stdin.readlines():
   [user,mark] = line.split()
   if user not in marks:
      marks[user] = 0
   marks[user] += int(mark)

for user in sorted(marks):
   print user, marks[user]

