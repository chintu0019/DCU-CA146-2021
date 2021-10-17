#!/usr/bin/env python3

n = int(input())
m = 765090

i = 0
while i < n:
   v = int(input())
   m = m + v * 320652 - 151423  # multiply by 320652 and subtract 151423.
   print(v * 695658)            # multiply by 695658.
   i = i + 1

print(m)
