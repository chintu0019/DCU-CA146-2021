#!/usr/bin/env python

import sys
a = sys.stdin.readlines()

i = 0
while i < len(a) and len(a[i].strip()) != 4:
   i = i + 1

if i < len(a):
   print a[i].strip()
else:
   print "none"
