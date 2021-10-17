#!/usr/bin/env python3

n = int(input())
s = ""

i = 0
while i < n:
   if 0 < i:
      s = s + " "
   s = s + str(i * 2 % 6)
   i = i + 1

print(s)
