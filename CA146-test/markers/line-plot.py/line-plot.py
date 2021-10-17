#!/usr/bin/env python

import sys

n = 20
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

def should_plot(x, y):
   if x < x1 and x < x2:  # Too far left.
      return False
   if x1 < x and x2 < x:  # Too far right.
      return False
   if y < y1 and y < y2:  # Too far down.
      return False
   if y1 < y and y2 < y:  # Too far up.
      return False
   # These are just two formulations of the line formula:
   #
   #   y = mx + c
   #   x = (y-c) / m  (equivalent)
   #
   # The first form draws lines well if the line is closer to horizontal.
   # The second form draws lines well if they are closer to vertical.
   # int() rounds down.  By adding 0.5, we get the nearest integer value.
   return x == int((y - c) / m + 0.5) or y == int(m * x + c + 0.5)

# Print header line.
print " " + "-" * n

i = 0
while i < n:
   y = n - i - 1
   output = []

   x = 0
   while x < n:
      if should_plot(x, y):
         output.append("*")
      else:
         output.append(" ")
      x = x + 1

   # Build and print the current line.
   print "|" + "".join(output) + "|"
   i = i + 1

# Print footer line.
print " " + "-" * n
