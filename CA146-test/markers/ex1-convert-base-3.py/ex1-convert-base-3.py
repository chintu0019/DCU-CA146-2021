#!/usr/bin/env python

import sys

number = sys.argv[1]
base = int(sys.argv[2])
v = 0

for d in number:
   v *= base
   v += int(d)

print v

