#!/usr/bin/env python

import sys

number = int(sys.argv[1])

line = raw_input()
while line != "end" and 0 < number:
   print line
   line = raw_input()
   number -= 1
