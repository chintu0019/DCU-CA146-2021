#!/usr/bin/env python3

n = int(input())
m = 318515

i = 0
while i < n:
   v = int(input())
   m = m + v * 323732 - 106561  # multiply by 323732 and subtract 106561.
   print(v * 737325)            # multiply by 737325.
   i = i + 1

print(m)
