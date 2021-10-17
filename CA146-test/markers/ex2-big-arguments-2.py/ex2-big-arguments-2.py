#!/usr/bin/env python3

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
   if 500 < int(args[i]):
      print(args[i])
   i = i + 1
