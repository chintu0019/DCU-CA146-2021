#!/usr/bin/env python3

n = 10
hist = [0] * n

line = input()
while line != "end":
   hist[int(line)] += 1
   line = input()

i = 0
while i < n:
   print(i, "*" * hist[i])
   i = i + 1
