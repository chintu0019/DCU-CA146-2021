#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   details = line.split()
   print " ".join(details[1:])

