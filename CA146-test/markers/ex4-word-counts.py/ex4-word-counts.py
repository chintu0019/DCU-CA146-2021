#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   print len(lines[i].split())
   i = i + 1
