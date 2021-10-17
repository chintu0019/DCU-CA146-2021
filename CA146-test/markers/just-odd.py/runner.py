#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

for n in [1, 3, 15, 123]:
   for m in [2, 10, 102]:
      print "n =", n, ", m =", m, ":",
      execfile(os.environ["TASK"])
      print "odd =", odd

for m in [1, 3, 15, 123]:
   for n in [2, 10, 102]:
      print "n =", n, ", m =", m, ":",
      execfile(os.environ["TASK"])
      print "odd =", odd
