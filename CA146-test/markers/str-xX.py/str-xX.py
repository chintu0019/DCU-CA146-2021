#!/usr/bin/env python

import sys

s = sys.argv[1]
t = ""

i = 0
while i < len(s):
   ch = s[i]
   if "a" <= ch and ch <= "z":
      t += "x"
   elif "A" <= ch and ch <= "Z":
      t += "X"
   else:
      t += ch

   i += 1

print t
