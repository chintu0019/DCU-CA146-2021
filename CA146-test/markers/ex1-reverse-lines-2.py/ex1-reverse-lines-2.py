#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

for i in range(len(lines)):
   print lines[len(lines)-1-i]

