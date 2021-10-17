#!/usr/bin/env python

import os

side = 20

print "side:", side
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable area is now", area

print

side = 30

print "side:", side
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable area is now", area

