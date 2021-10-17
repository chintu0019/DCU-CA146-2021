#!/usr/bin/env python

import os
task = os.environ["TASK"]

a = "".split()

print "a =", a
print "running your script..."
print

execfile(task)
