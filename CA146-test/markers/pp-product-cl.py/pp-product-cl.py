#!/usr/bin/env python

import sys
s = sys.argv[1]
product = 1

i = 0
while i < len(s):
   product = product * int(s[i])
   i = i + 1

print product
