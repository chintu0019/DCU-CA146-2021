#!/usr/bin/env python

a = []

line = raw_input()
while line != "end":
   a.append(int(line))
   line = raw_input()

# loop invariant:
#   - a[0:i] is sorted

i = 1
while i < len(a):
   # loop invariant:
   #   - each of a[j:i] is greater than v (the original a[i])
   v = a[i]
   j = i
   while 0 < j and v < a[j - 1]:
      a[j] = a[j - 1]
      j = j - 1
   a[j] = v

   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1
