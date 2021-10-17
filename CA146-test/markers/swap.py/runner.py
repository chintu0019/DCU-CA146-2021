#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

for n in [1, 3, 22, 123, 1024]:
   for m in [2, 7, 17, 78, 127]:
      print "before: n =", n, ", m =", m, "after:",
      execfile(os.environ["TASK"])
      print "n =", n, ", m =", m
