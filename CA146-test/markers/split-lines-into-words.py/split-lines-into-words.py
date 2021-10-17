#!/usr/bin/env python

# Example line:
# and blah, blah abracadabra blah
#                |          |
#                | i        | j

line = raw_input()
while line != "end":
   i = 0
   while i < len(line):

      while i < len(line) and line[i] == ' ':
         i = i + 1

      j = i
      while j < len(line) and line[j] != ' ':
         j = j + 1

      if i < j:
         print line[i:j]

      i = j

   line = raw_input()
