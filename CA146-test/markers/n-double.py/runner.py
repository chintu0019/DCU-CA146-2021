#!/usr/bin/env python

import os

n = 3

print "variable n is", n
for v in range(10):
   print "executing", os.environ.get("TASK"), "..."
   execfile(os.environ.get("TASK"))
   print "variable n is", n
