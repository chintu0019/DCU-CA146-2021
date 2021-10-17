#!/usr/bin/env python

import sys, os
task = os.environ["TASK"]

with open(task) as f:
   lines = [line.rstrip() for line in f.readlines()]

i = 0
while i < len(lines):
   s = lines[i]
   j = 0
   while j < len(s) and s[j].isspace():
      j = j + 1
   lines[i] = s[:j]
   i = i + 1

print "Validating indentation..."
print

valid_indents = set([2, 3, 4])
ok = True

i = 0
while i < len(lines):
   s = lines[i]
   if "\t" in s:
      print "error: TAB character found on line", i + 1
      i = i + 1
      ok = False
      continue

   indents = []
   if len(s) % 2 == 0: indents.append(2)
   if len(s) % 3 == 0: indents.append(3)
   if len(s) % 4 == 0: indents.append(4)

   valid_indents = valid_indents.intersection(set(indents))
   i = i + 1

   if len(valid_indents) == 0:
      print "No consistent indentation remains on line", i
      print
      print "Use indentation of two, three or four SPACE characters."
      print "Do not use TAB characters for indentation."
      print "Use consistent indentation (pick a number of spaces and stick to it)."
      print
      sys.exit(1)

if ok:
   print "ok"
   print
else:
   print
   sys.exit(1)

