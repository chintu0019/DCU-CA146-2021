#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

i = -5
while i < 15:
   x = i
   execfile(os.environ["TASK"])
   print "x =", i, "-->", x
   i = i + 1
