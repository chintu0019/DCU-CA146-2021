#!/usr/bin/env python

ints = []

line = raw_input()
while line != "end":
   ints.append(int(line))
   line = raw_input()

i = 0
while i < len(ints):
   j = len(ints) - i - 1
   if ints[j] % 2 == 0:
      print ints[j]
   i += 1

