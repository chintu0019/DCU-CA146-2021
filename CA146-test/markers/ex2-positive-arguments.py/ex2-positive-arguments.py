#!/usr/bin/env python

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
   if 0 < int(args[i]):
      print args[i]
   i = i + 1
