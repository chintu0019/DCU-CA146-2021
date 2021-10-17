#!/usr/bin/env python

ints = []

line = raw_input()
while line != "end":
   ints.append(int(line))
   line = raw_input()

i = 0
while i < len(ints) and ints[i] % 2 != 0:
   i += 1

if i < len(ints):
   print i
