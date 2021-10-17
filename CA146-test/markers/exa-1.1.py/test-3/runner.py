#!/usr/bin/env python

import os
task = os.environ["TASK"]

a = "89 34 789 8779 5675 09980 45 3 2   6 77".split()

print "a =", a
print "running your script..."
print

execfile(task)
