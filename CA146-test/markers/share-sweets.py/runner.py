#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

for sweets in range(10,20):
   for children in range(1,5):
      print "sweets =", sweets, ", children =", children, ":",
      execfile(os.environ["TASK"])
      print sweets_per_child, sweets_left_over_child
