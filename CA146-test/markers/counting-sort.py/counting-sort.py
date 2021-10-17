#!/usr/bin/env python3

n = 1000
counts = [0] * 1000

line = input()
while line != "end":
   counts[int(line)] += 1
   line = input()

i = 0
while i < n:
   if 0 < counts[i]:
      output = ("\n" + str(i)) * counts[i]
      print(output[1:])
   i = i + 1
