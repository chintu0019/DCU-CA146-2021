#!/usr/bin/env python3

n = int(input())
d = n % 10

if n < 0:
   d = 10 - d

if d == 3:
   print("yes")
else:
   print("no")
