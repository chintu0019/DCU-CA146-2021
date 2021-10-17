#!/usr/bin/env python

import os
task = os.environ["TASK"]

s = "123 " * 53

print "s =", '"{}"'.format(s)
print "running your script..."
print

execfile(task)
