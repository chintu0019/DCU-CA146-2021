#!/usr/bin/env python

line = raw_input()
while line != "end":
   product = 1

   i = 0
   while i < len(line):
      product = product * int(line[i])
      i = i + 1

   print product
   line = raw_input()

