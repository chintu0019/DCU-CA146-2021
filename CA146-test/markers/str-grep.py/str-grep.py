#!/usr/bin/env python

import sys

needle = sys.argv[1]
line = raw_input()

while line != "end":
   if 0 <= line.find(needle):
      print line
   line = raw_input()
