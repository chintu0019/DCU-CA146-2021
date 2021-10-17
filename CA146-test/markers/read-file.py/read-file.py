#!/usr/bin/env python3

import sys

with open("input.txt") as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   sys.stdout.write(lines[i])
   i = i + 1
