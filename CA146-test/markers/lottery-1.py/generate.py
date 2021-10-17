#!/usr/bin/env python

import sys
from random import randint

[pick, balls, n] = map(int, sys.argv[1:])
seen = {}

for i in range(n):
   bs = []
   while len(set(bs)) < pick:
      bs.append(randint(1,balls))

   combination = " ".join(map(str,sorted(set(bs))))
   if combination not in seen:
      seen[combination] = True
      print " ".join(map(str,sorted(set(bs))))
