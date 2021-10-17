#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   mark = int(line.split()[4])

   if mark < 40:
      c = "F"
   elif mark < 50:
      c = "3"
   elif mark < 60:
      c = "2.2"
   elif mark < 70:
      c = "2.1"
   else:
      c = "1"

   print " ".join(line.split()[:5]), c, " ".join(line.split()[5:])
