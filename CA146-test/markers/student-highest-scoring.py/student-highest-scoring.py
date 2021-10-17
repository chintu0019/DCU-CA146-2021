#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

if 0 < len(lines):
   m = int(lines[0].split()[4])
   p = 0

   i = 0
   while i < len(lines):
      if m < int(lines[i].split()[4]):
         p = i
         m = int(lines[i].split()[4])
      i = i + 1

   print " ".join(lines[p].split()[5:])
