#!/usr/bin/env python

largest = 0

i = 0
while i < 6:
   n = input()
   if largest < n:
      largest = n
   i = i + 1

print largest
