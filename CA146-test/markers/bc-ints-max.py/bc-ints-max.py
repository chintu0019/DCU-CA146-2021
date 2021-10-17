#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(int(line))
   line = raw_input()

if 0 == len(lines):
   print 0
else:
   m = lines[0]

   i = 1
   while i < len(lines):
      if m < lines[i]:
         m = lines[i]
      i = i + 1

   print m

