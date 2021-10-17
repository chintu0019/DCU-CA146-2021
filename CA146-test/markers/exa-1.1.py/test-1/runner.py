#!/usr/bin/env python

import os
task = os.environ["TASK"]

a = "dog chicken cat mouse stoat hen weasel squirrel".split()

print "a =", a
print "running your script..."
print

execfile(task)
