#!/usr/bin/env python

count = 0
total = 0

line = raw_input()
while line != "end":
   count += 1
   total += int(line)
   line = raw_input()

if 0 < count:
   print total / count
else:
   print 0

