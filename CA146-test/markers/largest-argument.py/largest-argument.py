#!/usr/bin/env python

import sys
largest = int(sys.argv[1])

i = 2
while i < len(sys.argv):
   if largest < int(sys.argv[i]):
      largest = int(sys.argv[i])
   i = i + 1

print largest
