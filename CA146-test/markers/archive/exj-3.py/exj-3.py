#!/usr/bin/env python

n = 20

import sys

# Approach...
#
# We maintain a dictionary "plot" the keys of which are of the form
# "x-y", for example, "19-16".  When generating the output, we consult
# this dictionary to decide whether to print a space or an asterisk
# at position (x, y).
#
# The values in the dictionary do not matter.  It is the presence (or
# absence) of the key which matters.

lines = sys.stdin.readlines()
plot = {}

i = 0
while i < len(lines):
   tokens = lines[i].split()
   key = tokens[0] + "-" + tokens[1]  # This is "x-y", e.g. "19-16".
   plot[key] = True
   i = i + 1

# Print header line.
print " " + "-" * n

# We have to print the plot from top to bottom.  Therefore, we must
# visit the y coordinates in reverse order.
#
# The outer loop here is for the y coordinates (the rows or lines), and
# the inner loop is for the x coordinates.

i = 0
while i < n:
   y = n - i - 1
   output = []

   x = 0
   while x < n:
      key = str(x) + "-" + str(y)  # This is the same key format as above.
      if key in plot:
         output.append("*")
      else:
         output.append(" ")
      x = x + 1

   # Build and print the current line.
   print "|" + "".join(output) + "|"
   i = i + 1

# Print footer line.
print " " + "-" * n
