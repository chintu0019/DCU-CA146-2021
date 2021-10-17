#!/usr/bin/env python3

n = 10000000  # Ten million.
a = []

i = 0
while i < n:
   #
   a.append(i)
   #
   if i % 100000 == 0:  # One hundred thousand.
      print(i)
   #
   i = i + 1
