#!/usr/bin/env python

import sys

file = "translation.txt"

with open(file) as f:
   for line in f.readlines():
      sys.stdout.write(line)

