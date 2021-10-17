#!/usr/bin/env python

import sys

n = int(sys.argv[1])

i = 2
while i < n:
   if i % 2 == 1:
      print i
   i = i + 1
