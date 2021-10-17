#!/usr/bin/env python

import sys

file = sys.argv[1]

with open(file) as f:
   for line in f.readlines():
      sys.stdout.write(line)

