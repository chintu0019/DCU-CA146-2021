#!/usr/bin/env python

import os

print "executing assignment statement..."
execfile(os.environ.get("TASK"))
print "variable n is now", n

