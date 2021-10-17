#!/usr/bin/env python

import os

a = os.listdir(".")

# Insertion sort.
i = 1
while i < len(a):
   v = a[i]
   j = i
   while 0 < j and v < a[j-1]:
      a[j] = a[j-1]
      j = j - 1
   a[j] = v
   i = i + 1

i = 0
while i < len(a):
   if os.path.isfile(a[i]):
      a[i] = "f " + a[i]
   else:
      a[i] = "d " + a[i]
   print a[i]
   i = i + 1
