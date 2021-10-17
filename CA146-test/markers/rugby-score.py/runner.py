#!/usr/bin/env python

import os

print "running", os.environ["TASK"], "multiple times..."
print

for tries in range(0, 4):
   for conversions in range(0, tries + 1):
      for penalties in range(0, 4):
         print "tries =", tries, ", conversions =", conversions, ",penalties =", penalties, ":",
         execfile(os.environ["TASK"])
         print "score =", score
