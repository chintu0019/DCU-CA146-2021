#!/usr/bin/env python3

import sys
s = sys.argv[1]

# First, parse the argument to extract the field name and the
# required value.
#
i = 0
while i < len(s) and s[i] != "=":
   i = i + 1

field = s[:i]
value = s[i + 1:]

s = input()
position = 0
start = 0

# The following is more or less the solution to
# the "csv-field-name.py" task.
#
# First find the start and end of the first header field.
#
end = 0
while end < len(s) and s[end] != ",":
   end = end + 1

# Have we found the field which we are looking for?
#
while s[start:end] != field:
   # Find the start and end of the next header field.
   #
   position = position + 1
   start = end + 1

   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1

# Next, consider each data line in turn.
#
s = input()
while s != "end":
   # The body of the loop here is more or less the solution
   # to the "csv-field-name.py" task.
   #
   start = 0

   i = 0
   while i < position:
      while start < len(s) and s[start] != ",":
         start = start + 1

      start = start + 1
      i = i + 1

   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1

   if s[start:end] == value:
      print(s)

   s = input()
