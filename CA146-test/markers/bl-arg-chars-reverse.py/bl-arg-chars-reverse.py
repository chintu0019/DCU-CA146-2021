#!/usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s):
   print s[len(s)-1-i]
   i = i + 1

