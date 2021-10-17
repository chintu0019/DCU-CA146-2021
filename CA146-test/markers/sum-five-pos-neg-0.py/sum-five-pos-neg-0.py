#!/usr/bin/env python3

neg = 0
pos = 0

v = int(input())
while v != 0:
   if v < 0:
      neg = neg + v
   else:
      pos = pos + v
   v = int(input())

print(neg, pos)
