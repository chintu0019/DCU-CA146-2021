#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

for bits in range(1, 33):
   print "bits =", bits, ":",
   execfile(os.environ["TASK"])
   print "values =", values
