#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

if 0 < len(lines):
   t = 0.0
   for line in lines:
      t += int(line.split()[4])

   print t / len(lines)



else:
   print 0.0
