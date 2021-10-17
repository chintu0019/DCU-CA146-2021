#!/usr/bin/env python

import os
task = os.environ["TASK"]

a = "dog cat mouse hen".split()

print "a =", a
print "running your script..."
print

execfile(task)
