#!/usr/bin/env python

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
   if int(args[i]) % 2 == 1:
      print args[i]
   i = i + 1
