#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

pi = 3.141

for radius in range(1, 10):
   print "radius =", radius, ":",
   execfile(os.environ["TASK"])
   print "circumference =", circumference, ", area =", area
