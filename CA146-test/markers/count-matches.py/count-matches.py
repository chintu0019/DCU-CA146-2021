#!/usr/bin/env python

import sys
pattern = sys.argv[1]

line = raw_input()
while line != "end":
   count = 0

   i = 0
   while i < len(line):
      # Linear search, starting at position i.
      while i < len(line) and line[i:i+len(pattern)] != pattern:
         i = i + 1

      # Either:
      #   We have found PATTERN in line.
      #                 |
      #                 i
      # Or:
      #   There is no match in this line.
      #                                  |
      #                                  i

      if i < len(line):
         # A match was found; count it...
         count = count + 1
         # ...and jump to the character after the match.
         i = i + len(pattern)

   print count
   line = raw_input()
