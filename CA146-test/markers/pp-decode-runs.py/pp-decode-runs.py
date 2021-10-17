#!/usr/bin/env python

t = ""

s = raw_input()
while s != "END":
   t = t + s[0] * int(s[2:])
   s = raw_input()

print t
