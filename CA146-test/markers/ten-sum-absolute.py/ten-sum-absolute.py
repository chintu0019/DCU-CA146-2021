#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
   v = int(input())
   if v < 0:
      v = -v
   assert 0 <= v
   total = total + v
   i = i + 1

print(total)
