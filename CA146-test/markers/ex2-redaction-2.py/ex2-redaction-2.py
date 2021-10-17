#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   tokens = line.split()
   for token in tokens:
      print token
