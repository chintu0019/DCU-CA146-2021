#!/usr/bin/env python

import sys

s = sys.stdin.readline()
while 0 < len(s) and int(s) < 100:
   s = sys.stdin.readline()

if 0 < len(s):
   sys.stdout.write(s)
else:
   print "none"
