#!/usr/bin/env python

a = []

line = raw_input()
while line != "end":
   a.append(int(line))
   line = raw_input()

v = int(raw_input())
a.append(None)                 # The value here does not matter.

p = len(a) - 1                 # Linear search, but backwards.
while 0 < p and v < a[p - 1]:  #
   a[p] = a[p - 1]             # Move a[p-1] up, to make space.
   p = p - 1                   #

a[p] = v                       # Put v in its final position.
print a
