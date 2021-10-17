#!/usr/bin/env python

import os
task = os.environ["TASK"]

a = range(12)
a = map(str, a)
s = " ".join(a)

print "s =", '"{}"'.format(s)
print "running your script..."
print

execfile(task)
