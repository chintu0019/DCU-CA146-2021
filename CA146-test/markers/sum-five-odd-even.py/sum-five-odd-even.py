#!/usr/bin/env python

total = 0
xx = 0

i = 0
while i < 5:
   v = input()
   if v < 0:
      xx += v
   else:
      total += v
   i += 1

print xx, total

