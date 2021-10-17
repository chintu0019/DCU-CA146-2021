#!/usr/bin/env python3

n = int(input())
m = 158362

i = 0
while i < n:
   v = int(input())
   m = m + v * 308091 - 526630  # multiply by 308091 and subtract 526630.
   print(v * 720232)            # multiply by 720232.
   i = i + 1

print(m)
