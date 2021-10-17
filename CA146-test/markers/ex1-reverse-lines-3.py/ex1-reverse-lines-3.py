#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

for i in range(len(lines)):
   s = lines[i]
   t = ""
   while 0 < len(s):
      t = s[0] + t
      s = s[1:]
   lines[i] = t

for i in range(len(lines)):
   print lines[len(lines)-1-i]

