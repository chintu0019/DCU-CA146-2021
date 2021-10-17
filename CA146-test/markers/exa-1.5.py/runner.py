#!/usr/bin/env python

import os
task = os.environ["TASK"]

s = "dog  cat   mouse hen"

print "s =", '"{}"'.format(s)
print "running your script..."
print

execfile(task)
