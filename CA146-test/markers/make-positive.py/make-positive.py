#!/usr/bin/env python

s = raw_input()
while s != "end":
   if s[0] == "-":
      s = s[1:]
   print s
   s = raw_input()
