#!/usr/bin/env python

import sys

n = 20
x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
side = int(sys.argv[3])

x2 = x1 + side - 1
y2 = y1 + side - 1

def should_plot(x, y):
   if y == y1 and x1 <= x and x <= x2:    # Bottom.
      return True
   elif y == y2 and x1 <= x and x <= x2:  # Top.
      return True
   elif x == x1 and y1 <= y and y <= y2:  # Left.
      return True
   elif x == x2 and y1 <= y and y <= y2:  # Right.
      return True
   else:
      return False

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
