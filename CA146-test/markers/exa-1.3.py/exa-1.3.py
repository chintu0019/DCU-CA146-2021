#!/usr/bin/env python

import sys
file_name = sys.argv[1]

with open(file_name) as f:
   if len(f.read()) == 0:
      print "empty"
   else:
      print "non-empty"
