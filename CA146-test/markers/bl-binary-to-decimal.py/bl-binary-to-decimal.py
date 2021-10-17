#!/usr/bin/env python

import sys

b = sys.argv[1]
v = 0

while b:
   v *= 2
   if b[0] == "1":
      v += 1
   b = b[1:]

print v
