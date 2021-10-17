#!/usr/bin/env python3

a = []

# We do not change the selection-sort algorithm itself.  Instead,
# we reorganise the characters on each line as they are read.  We
# read this...
#
#   05/05/88 Adele Laurie Blue Adkins
#
# and rearrange the characters to get a line like this...
#
#   880505Adele Laurie Blue Adkins
#
# In this format, regular string comparison produces the required
# order.

line = input()
while line != "end":
   #      year        month       day          name
   #      |           |           |            |
   line = line[6:8] + line[3:5] + line[0:2] + line[9:]
   a.append(line)
   line = input()

# This is the selection-sort algorithm, entirely unchanged.

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

# And print out the lines, with the leading dates stripped off. Looking
# at line 22, above, we see that the name starts at position 6.

i = 0
while i < len(a):
   print(a[i][6:])
   i = i + 1
