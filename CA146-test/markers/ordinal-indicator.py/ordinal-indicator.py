#!/usr/bin/env python3

# This is the task that I got wrong in the lecture.  It has been fixed now.

n = int(input())

if 11 <= n % 100 and n % 100 <= 13:  # xxx11, xxx12, and xxx13
   print("th")
elif n % 10 == 1:                    # xxx1
   print("st")
elif n % 10 == 2:                    # xxx2
   print("nd")
elif n % 10 == 3:                    # xxx3
   print("rd")
else:
   print("th")                       # Everything else.
