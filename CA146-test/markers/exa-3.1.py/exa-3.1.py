#!/usr/bin/env python

n = input()

print "*" * (n + 2)

i = 0
while i < n:
   if i == n / 2:
      print "*" * (n + 2)
   else:
      print "*" + " " * (n / 2) + "*" + " " * (n / 2) + "*"
   i = i + 1

print "*" * (n + 2)
