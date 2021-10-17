#!/usr/bin/env python3

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
   with open(args[i]) as f:
      if 0 < len(f.read(1)):
         print(args[i])
   i = i + 1
