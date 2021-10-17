#!/usr/bin/env python

n = input()

i = 0
while i < n:
   print "." * i + "*" + "." * (n - i - 1)
   i = i + 1
