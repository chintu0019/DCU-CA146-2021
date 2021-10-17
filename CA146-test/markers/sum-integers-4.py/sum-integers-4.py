#!/usr/bin/env python3

import sys

# It is conventional to add an "s" to a variable name to signify that it is
# a list (so , plural).  Here, "ns" is a list of numbers.
ns = []

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as f:
      # Using "f.read().split()" to read the numbers here solves two problems.
      # It deals with:
      #   - the case where there are multiple numbers on the same line, and
      #   - the case where there are no numbers on a line.
      ns = ns + f.read().split()
   i = i + 1

total = 0

i = 0
while i < len(ns):
   total = total + int(ns[i])
   i = i + 1

print(total)
