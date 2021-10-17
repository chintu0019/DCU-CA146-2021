#!/usr/bin/env python

import sys

n = int(sys.argv[1])
factor = 2

while 1 < n:
   while n % factor == 0:
      print factor
      n = n / factor
   factor = factor + 1

