#!/usr/bin/env python

a = []

line = raw_input()
while line != "end":
   a.append(line)
   line = raw_input()

line = raw_input()
while line != "end":
   i = int(line)
   print a[i]
   line = raw_input()
