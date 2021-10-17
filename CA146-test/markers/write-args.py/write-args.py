#!/usr/bin/env python3

import sys

with open(sys.argv[1], "w") as f:
   i = 2
   while i < len(sys.argv):
      f.write(sys.argv[i] + "\n")
      i = i + 1
