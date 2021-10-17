#!/usr/bin/env python

import sys

count = 1
mapping = {}

line = sys.stdin.readline()
while line:
   toks = line.split()
   name = toks[3]
   if name not in mapping:
      mapping[name] = "user-" + str(count)
      count += 1
   toks[3] = mapping[name]
   print " ".join(toks)
   line = sys.stdin.readline()
