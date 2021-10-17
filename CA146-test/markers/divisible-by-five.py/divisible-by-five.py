#!/usr/bin/env python

s = raw_input()
while s != "end":
   t = s[len(s)-1]
   if t == "0" or t == "5":
      print s
   s = raw_input()
