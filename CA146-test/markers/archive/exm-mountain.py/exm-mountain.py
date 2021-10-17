#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   s = " " * (n - i - 1) + "*"
   if i != 0:
      s = s + " " * (2 * i - 1) + "*"
   print(s)
   i = i + 1
