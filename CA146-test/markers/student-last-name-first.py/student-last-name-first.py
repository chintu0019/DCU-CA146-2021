#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   details = line.split()
   name = details[5:]
   last = name.pop()
   name = last + ", " + " ".join(name)
   print " ".join(details[:5]) + " " + name


