#!/usr/bin/env python

longest = ""
found = False

line = raw_input()
while line != "end":
   found = True
   if len(longest) < len(line):
      longest = line
   line = raw_input()

if found:
   print longest

